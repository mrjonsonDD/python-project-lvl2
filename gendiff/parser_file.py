import os
import json
import yaml
from json.decoder import JSONDecodeError
from yaml.scanner import ScannerError


YAML_ERROR_MSG = '{0} - incorrect YAML file'
JSON_ERROR_MSG = '{0} - incorrect JSON file'


def get_format(file_path):
    file_format = os.path.splitext(file_path)[1]
    return file_format


def open_file(file_path):
    with open(os.path.abspath(file_path)) as f:
        file = f.read()
    return file


def prepare_file(file_path):
    file_format = get_format(file_path)
    file = open_file(file_path)
    return parser(file_format)(file)


def parser(file_format):
    format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    try:
        return format[file_format.lower()]
    except ScannerError:
        raise YAML_ERROR_MSG.format(file_format)
    except JSONDecodeError:
        raise JSON_ERROR_MSG.format(file_format)
