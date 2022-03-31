import json
import yaml
from json.decoder import JSONDecodeError
from yaml.scanner import ScannerError


YAML_ERROR_MSG = '{0} - incorrect YAML file'
JSON_ERROR_MSG = '{0} - incorrect JSON file'


def parser(data_format):
    format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    try:
        return format[data_format.lower()]
    except ScannerError:
        raise ScannerError(YAML_ERROR_MSG.format(data_format))
    except JSONDecodeError:
        raise JSONDecodeError(JSON_ERROR_MSG.format(data_format))
