"""Read sourse module."""
import json
import os

import yaml


def parser(file_extension):
    format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    return format[file_extension.lower()]


def parse_file(file_path):
    file_extension = get_extension(file_path)
    file = open_file(file_path)
    return parser(file_extension)(file)


def get_extension(file_path):
    file_extension = os.path.splitext(file_path)[1]
    return file_extension


def open_file(file_path):
    with open(os.path.abspath(file_path)) as f:
        file = f.read()
    return file
