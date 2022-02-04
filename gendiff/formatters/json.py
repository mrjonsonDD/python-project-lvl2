import json


def format_json(diff):
    return json.dumps(sort_difference(diff))


def sort_difference(diff):
    result = {}
    sort_list_keys = sorted(diff.keys())
    for key in sort_list_keys:
        result[key] = diff[key]
        if isinstance(diff[key], list):
            if isinstance(diff[key][1], dict):
                result[key][1] = sort_difference(diff[key][1])
    return result
