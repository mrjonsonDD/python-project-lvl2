"""This is json formatter."""
import json


def get_json(diff_structure):
    """Convert format_dict to json format.
    Parameters:
        diff_structure(format_dict): dict of difference.
    Returns:
        result json file.
    """
    return json.dumps(diff_structure, indent=2, sort_keys=True)
