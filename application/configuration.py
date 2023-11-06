"""Contains class that mappes configuration in json format to class attributes
It makes it easier to change the name of a key-value in a JSON file because we can easily find all the places where we used this key.
However, without mapping, the search would be less efficient and more likely to result in a typo."""

import json


class Configuration:
    def __init__(self, config_file_name):
        with open(config_file_name) as config:
            json_data = json.load(config)

        self.table_name = json_data['table_name']
        self.path_to_database = json_data['path_to_database']
