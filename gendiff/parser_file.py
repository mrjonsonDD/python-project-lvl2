import os
import json
import yaml
from json.decoder import JSONDecodeError
from yaml.scanner import ScannerError


YAML_ERROR_MSG = '{0} - incorrect YAML file'
JSON_ERROR_MSG = '{0} - incorrect JSON file'


def prepare_file(file_path):
    load_format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }
    file_format = os.path.splitext(file_path)[1]
    open_type = load_format.get(file_format)
    with open(os.path.abspath(file_path)) as f:
        file = f.read()
    try:
        return open_type(file)
    except ScannerError:
        raise YAML_ERROR_MSG.format(file_path)
    except JSONDecodeError:
        raise JSON_ERROR_MSG.format(file_path)
