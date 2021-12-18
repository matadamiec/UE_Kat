import json

from rest_api.models.links import Link


def make_links_list(json_input) -> [Link]:
    objects_from_json = json.loads(json_input)
    output_list = []
    for json_object in objects_from_json:
        output_list.append(Link(json_object['movieId'], json_object['imdbId'], json_object['tmdbId']))

    return output_list


def get_links_dict(links_list):
    output_list = []
    for item in links_list:
        output_list.append(item.__dict__)

    return output_list
