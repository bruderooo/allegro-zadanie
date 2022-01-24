import requests
from flask_restx import Resource, Namespace

list_repos_ns = Namespace('list_repos', description='API - Allegro task')


@list_repos_ns.route('/<string:username>', methods=['GET'])
class ListReposWithLanguages(Resource):

    @list_repos_ns.doc(
        description="Dla danego użytkownika zwraca słownik, gdzie kluczami są nazwy repozytoriów, "
                    "a odpowiadające im wartości, to listy użytych języków",
        params={'username': 'Nazwa użytkownika, dla którego pobieramy listę repozytoriów wraz z językami'}
    )
    def get(self, username: str):
        """Zwraca słownik repozytoriów dla danego użytkownika wraz z językami"""
        to_return: dict = {}

        repos_list: list = requests.get(f'https://api.github.com/users/{username}/repos').json()

        for repo in repos_list:
            to_return[repo['name']] = requests.get(repo['languages_url']).json()

        return to_return
