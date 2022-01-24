import requests
from flask_restx import Resource, Namespace

percentage_of_languages_ns = Namespace('percentage', description='API - Allegro task')


def compute_percentage_of_languages(languages_for_repos):
    languages = {}
    sum_all_code_bytes = 0

    for repos in languages_for_repos:
        for language, byte_value in repos.items():
            sum_all_code_bytes += byte_value
            languages[language] = languages.get(language, 0) + byte_value

    return {language: (byte_value / sum_all_code_bytes) * 100 for language, byte_value in languages.items()}


@percentage_of_languages_ns.route('/<string:username>', methods=['GET'])
class PercentageOfLanguages(Resource):

    @percentage_of_languages_ns.doc(
        description="Zwraca procentowe użycie języków w repozytoriach danego użytkownika",
        params={'username': 'Nazwa użytkownika, dla którego chcesz uzyskać procentową liczbę języków'}
    )
    def get(self, username: str):
        """Zwraca procentowe użycie języków w repozytoriach danego użytkownika"""
        repos_list: list = requests.get(f'https://api.github.com/users/{username}/repos').json()
        languages_for_repos = [requests.get(repo['languages_url']).json() for repo in repos_list]

        return compute_percentage_of_languages(languages_for_repos)
