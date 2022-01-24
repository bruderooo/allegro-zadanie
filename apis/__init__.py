from flask_restx import Api

from apis.list_repos import list_repos_ns as ns1
from apis.percentage_of_languages import percentage_of_languages_ns as ns2

api = Api(title='API - Allegro task')

api.add_namespace(ns1)
api.add_namespace(ns2)
