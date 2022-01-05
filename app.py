import argparse
import json

import requests
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, title='API - Allegro task')
app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get"]

namespace = api.namespace('', description='API - Allegro task')


@namespace.route('/list_repos/<string:username>', methods=['GET'])
class ListReposWithLanguages(Resource):

    @namespace.doc(
        description="Zwraca listę repozytoriów dla danego użytkownika",
        params={'username': 'Nazwa użytkownika, dla którego pobieramy listę repozytoriów wraz z językami'}
    )
    def get(self, username: str):
        """Zwraca listę repozytoriów dla danego użytkownika"""
        to_return: list = []

        repos_list: list = json.loads(requests.get(f'https://api.github.com/users/{username}/repos').text)

        for repo in repos_list:
            name: str = repo['name']
            r = requests.get(f'https://api.github.com/repos/{username}/{name}/languages')
            to_return.append((name, list(json.loads(r.text))))

        return to_return


@namespace.route('/percentage/<string:username>', methods=['GET'])
class PercentageOfLanguages(Resource):

    @namespace.doc(
        description="Zwraca procentową ilość języków w repozytoriach danego użytkownika",
        params={'username': 'Nazwa użytkownika, dla którego chcesz uzyskać procentową liczbę języków'}
    )
    def get(self, username: str):
        """Zwraca procentową ilość języków w repozytoriach danego użytkownika"""
        repos_list = json.loads(requests.get(f'https://api.github.com/users/{username}/repos').text)

        sum_all_code_bytes = 0
        languages = {}

        for repo in repos_list:
            r = requests.get(f'https://api.github.com/repos/{username}/{repo["name"]}/languages')
            for language, byte_value in json.loads(r.text).items():
                sum_all_code_bytes += byte_value
                languages[language] = languages.get(language, 0) + byte_value

        return {language: (byte_value / sum_all_code_bytes) * 100 for language, byte_value in languages.items()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Uruchamia aplikację API stworzoną na zaliczenie zadania.')
    parser.add_argument('--ip', dest='ip', default='127.0.0.1',
                        help='Adres IP do uruchomienia serwera (domyślnie przyjmuje adres 127.0.0.1')
    parser.add_argument('--port', dest='port', default='5000',
                        help='Port na którym ma działać serwer (domyślnie przyjmuje port 5000)')
    args = parser.parse_args()

    app.run(host=args.ip, port=args.port)
