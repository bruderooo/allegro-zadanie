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

    @namespace.doc(params={'username': 'Username for which you want to get list of repositories, with languages'})
    def get(self, username: str):
        """
        Returns a list of repos for a given user

        :param username: The username for which get the list of repos
        :return: A list of repos with languages
        """
        to_return: list = []

        repos_list: list = json.loads(requests.get(f'https://api.github.com/users/{username}/repos').text)

        for repo in repos_list:
            name: str = repo['name']
            r = requests.get(f'https://api.github.com/repos/{username}/{name}/languages')
            to_return.append((name, list(json.loads(r.text))))

        return to_return


@namespace.route('/percentage/<string:username>', methods=['GET'])
class PercentageOfLanguages(Resource):

    @namespace.doc(params={
        'username': 'Username for which you want to get percentage of languages on all repositories'})
    def get(self, username: str):
        """
        Return the percentage of languages used by a user in his repositories

        :param username: The username for which get the percentage of used languages
        :return:
        """
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
    app.run()
