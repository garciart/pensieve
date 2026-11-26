"""Convert data from JSON or YAML file to a Python dictionary.

Usage: python -B read_file_snip.py
"""

import json
import yaml

def yaml_to_dict(filepath:str) -> dict:
    """Read and convert a YAML file to a Python dictionary.

    :param str filepath: The location of the YAML file.
    :return dict: The YAML data as a Python dictionary.
    """
    _data = {}
    with open(filepath, 'r', encoding='UTF-8') as file:
        _data = yaml.safe_load(file)

    return _data

def json_to_dict(filepath:str) -> dict:
    """Read and convert a JSON file to a Python dictionary.

    :param str filepath: The location of the JSON file.
    :return dict: The YAML data as a Python dictionary.
    """
    _data = {}
    with open(filepath, 'r', encoding='UTF-8') as file:
        _data = json.load(file)

    return _data

if __name__ == '__main__':
    _planets_json = json_to_dict('planets.json')
    # print(_planets_json, type(_planets_json))
    print(_planets_json['earth']['name'])

    _planets_yaml = yaml_to_dict('planets.yml')
    # print(_planets_yaml, type(_planets_yaml))
    print(_planets_yaml['jupiter']['moons'])
