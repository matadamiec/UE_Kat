import json

from rest_api.models.ratings import Rating


def make_ratings_list(json_input) -> [Rating]:
    objects_from_json = json.loads(json_input)
    output_list = []
    for json_object in objects_from_json:
        output_list.append(Rating(json_object['userId'], json_object['movieId'], json_object['rating'], int(json_object['timestamp'])))

    return output_list


def get_ratings_dict(rating_list):
    output_list = []
    for item in rating_list:
        output_list.append(item.__dict__)

    return output_list
