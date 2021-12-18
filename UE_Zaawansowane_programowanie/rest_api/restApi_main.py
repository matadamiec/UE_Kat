import json

from flask import Flask
from flask_restful import Resource, Api

from rest_api.services import load_csv
from rest_api.services.links_utils import make_links_list, get_links_dict
from rest_api.services.movies_utils import get_movies_dict, make_movies_list
from rest_api.services.ratings_utils import get_ratings_dict, make_ratings_list
from rest_api.services.tags_utils import get_tags_dict, make_tags_list


def format_json(json_object):
    # create a formatted string of the Python JSON object
    text = json.dumps(json_object, sort_keys=True, indent=4)
    return text


app = Flask(__name__)
api = Api(app)


class WelcomePageApi(Resource):
    def get(self):
        return {'welcome:': 'MAD Api Welcome Page'}


class MoviesApi(Resource):
    def get(self):
        return {'movies': get_movies_dict(make_movies_list(load_csv.make_json("data_source/movies.csv")))}


class LinksApi(Resource):
    def get(self):
        return {'links': get_links_dict(make_links_list(load_csv.make_json("data_source/links.csv")))}


class RatingsApi(Resource):
    def get(self):
        return {'ratings': get_ratings_dict(make_ratings_list(load_csv.make_json("data_source/ratings.csv")))}


class TagsApi(Resource):
    def get(self):
        return {'tags': get_tags_dict(make_tags_list(load_csv.make_json("data_source/tags.csv")))}


api.add_resource(WelcomePageApi, '/')
api.add_resource(MoviesApi, '/movies')
api.add_resource(LinksApi, '/links')
api.add_resource(RatingsApi, '/ratings')
api.add_resource(TagsApi, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
