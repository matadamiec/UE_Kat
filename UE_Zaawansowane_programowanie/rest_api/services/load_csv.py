import csv
import json


def make_json(csv_file_path):
    data = []

    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for csv_item in csv_reader:
            data.append(csv_item)

    return json.dumps(data, indent=4)
