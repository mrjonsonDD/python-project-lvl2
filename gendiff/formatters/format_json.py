import json


def sorted_diff(diff):
    result = {}
    sort_list_keys = sorted(diff.keys())
    for key in sort_list_keys:
        result[key] = diff[key]
        if isinstance(diff[key], list):
            if isinstance(diff[key][1], dict):
                result[key][1] = sorted_diff(diff[key][1])
    return result


def to_json(diff):
    return json.dumps(sorted_diff(diff), indent=2)
