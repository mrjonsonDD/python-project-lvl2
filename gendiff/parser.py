import os
import json
import yaml


def prepare_file(file_path):
    file_format = get_format(file_path)
    file = open_file(file_path)
    file_type = parse_file(file_format)
    return file_type(file)


def get_format(file_path):
    return os.path.splitext(file_path)[1]


def open_file(file_path):
    with open(os.path.abspath(file_path)) as f:
        file = f.read()
    return file


def parse_file(file_format):
    format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    return format.get(file_format)
