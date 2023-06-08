"""
Json tools
"""

import json


class JSONReader:
    """
    A class to read JSON files.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        """
        Read the JSON file
        :return: contents as a Python object.
        """
        try:
            with open(self.file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("File not found.")
            return None
        except PermissionError:
            print("Permission denied to open the file.")
            return None

    def find_info(self, key):
        """
        Find specific information in the JSON data based on a given key.
        :param key:
        :return:
        """
        json_data = self.read_json()
        if key in json_data:
            return json_data[key]
        return None
