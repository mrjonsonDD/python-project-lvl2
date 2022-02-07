"""Read sourse module."""
import json
import os

import yaml


def parse_file(file_path):
    """Parse input_file into a dict.
    Args:
        file_path (path to file): input data.
    Returns:
         dict: dictionary of data.
    Raises:
        ValueError: if format of file is unsupported.
    """
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.json':
        with open(file_path) as json_file:
            return json.load(json_file)
    elif file_extension in {'.yaml', '.yml'}:
        with open(file_path) as yaml_file:
            return yaml.safe_load(yaml_file)
    raise ValueError('Unsupported file format')
