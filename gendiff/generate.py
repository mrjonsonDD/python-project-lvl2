from gendiff.parser import prepare_file
from gendiff.formatters.get_format import get_format
from gendiff.const import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED
    )


def generate_diff(file1, file2, format='stylish'):
    first_file = prepare_file(file1)
    second_file = prepare_file(file2)
    diff = make_diff(first_file, second_file)
    return get_format(diff, format)


def make_diff(first_file, second_file):
    diff = {}
    joint_keys = first_file.keys() and second_file.keys()
    deleted_keys = first_file.keys() - second_file.keys()
    added_keys = second_file.keys() - first_file.keys()
    for key in added_keys:
        diff[key] = [ADDED, second_file.get(key)]
    for key in deleted_keys:
        diff[key] = [DELETED, first_file.get(key)]
    for key in joint_keys:
        diff[key] = create_intersection_diff(
            first_file.get(key), second_file.get(key))
    return diff


def create_intersection_diff(value1, value2):
    child = isinstance(value1, dict) and isinstance(value2, dict)
    if child:
        return [NESTED, make_diff(value1, value2)]
    elif value1 == value2:
        return [UNCHANGED, value1]
    else:
        return [CHANGED, value1, value2]
