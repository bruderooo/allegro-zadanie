import json

import requests
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


class AllegroRecruitingTask(Resource):

    @api.route('/list_repos/<string:username>')
    def get(self, username: str):
        """
        Returns a list of repos for a given user

        :param username: The username for which get the list of repos
        :return: A list of repos with languages
        """
        to_return = []

        repos_list = json.loads(requests.get(f'https://api.github.com/users/{username}/repos').text)

        for repo in repos_list:
            name = repo['name']
            r = requests.get(f'https://api.github.com/repos/{username}/{name}/languages')
            to_return.append((name, list(json.loads(r.text))))

        return to_return

    @api.route('/percentage/<string:username>')
    def get(self, username: str):
        """
        Return the percentage of languages used by a user in his repos

        :param username: The username for which get the percentage of used languages
        :return:
        """
        repos_list = json.loads(requests.get(f'https://api.github.com/users/{username}/repos').text)

        sum_ = 0
        languages = {}

        for repo in repos_list:
            r = requests.get(f'https://api.github.com/repos/{username}/{repo["name"]}/languages')
            for language, byte_value in json.loads(r.text).items():

                sum_ += byte_value

                if language in languages:
                    languages[language] += byte_value

        return {language: (byte_value / sum_) * 100 for language, byte_value in languages.items()}


if __name__ == '__main__':
    app.run()
