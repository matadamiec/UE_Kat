import json

from rest_api.models.tags import Tag


def make_tags_list(json_input) -> [Tag]:
    objects_from_json = json.loads(json_input)
    output_list = []
    for json_object in objects_from_json:
        output_list.append(Tag(json_object['userId'], json_object['movieId'], json_object['tag'], int(json_object['timestamp'])))

    return output_list


def get_tags_dict(tags_list):
    output_list = []
    for item in tags_list:
        output_list.append(item.__dict__)

    return output_list
