import json

import requests
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


class AllegroRecruitingTask(Resource):

    @api.route('/list_repos/<username>')
    def get(self, username):
        to_return = []

        repos_list = json.loads(requests.get(f'https://api.github.com/users/{username}/repos').text)

        for repo in repos_list:
            name = repo['name']
            r = requests.get(f'https://api.github.com/repos/{username}/{name}/languages')
            to_return.append((name, list(json.loads(r.text))))

        return to_return


if __name__ == '__main__':
    app.run()
