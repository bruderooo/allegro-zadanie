import requests
from flask_restx import Resource, Namespace

percentage_of_languages_ns = Namespace('percentage', description='API - Allegro task')


@percentage_of_languages_ns.route('/<string:username>', methods=['GET'])
class PercentageOfLanguages(Resource):

    @percentage_of_languages_ns.doc(
        description="Zwraca procentowe użycie języków w repozytoriach danego użytkownika",
        params={'username': 'Nazwa użytkownika, dla którego chcesz uzyskać procentową liczbę języków'}
    )
    def get(self, username: str):
        """Zwraca procentowe użycie języków w repozytoriach danego użytkownika"""
        repos_list: list = requests.get(f'https://api.github.com/users/{username}/repos').json()

        sum_all_code_bytes: int = 0
        languages: dict = {}

        for repo in repos_list:
            r = requests.get(repo['languages_url'])
            for language, byte_value in r.json().items():
                sum_all_code_bytes += byte_value
                languages[language] = languages.get(language, 0) + byte_value

        return {language: (byte_value / sum_all_code_bytes) * 100 for language, byte_value in languages.items()}
