import json

from rest_api.models.movie import Movie


def make_movies_list(json_input) -> [Movie]:
    objects_from_json = json.loads(json_input)
    output_list = []
    for json_object in objects_from_json:
        output_list.append(Movie(json_object['movieId'], json_object['title'], json_object['genres']))

    return output_list


def get_movies_dict(movies_list):
    output_list = []
    for item in movies_list:
        output_list.append(item.__dict__)

    return output_list
