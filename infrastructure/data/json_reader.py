"""
Json tools
"""

import os
import json


class JSONReader:
    """
    A class to read JSON files.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    @property
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
        data = self.read_json
        if key in data:
            return data[key]
        return None



# Specify the directory path
directory_path = "./"

# List the contents of the directory
directory_contents = os.listdir(directory_path)

# Print the directory contents
for item in directory_contents:
    print(item)