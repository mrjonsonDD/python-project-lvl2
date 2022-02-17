from gendiff.constants import (
    ADDED,
    CHANGED,
    CONDITION,
    DELETED,
    NESTED,
    UNCHANGED,
    VALUE,
)


def build_diff_tree(first_dict, second_dict):
    """Get difference tree betweet two file.
    Args:
        first_dict (string): Dict from the first file.
        second_dict (string): Dict from the second file.
    Returns:
        difference dict.
    """
    diff_diff = {}
    shared_keys = (first_dict.keys() & second_dict.keys())
    deleted_keys = (first_dict.keys() - second_dict.keys())
    added_keys = (second_dict.keys() - first_dict.keys())
    for key in deleted_keys:
        diff_diff[key] = {CONDITION: DELETED, VALUE: first_dict[key]}
    for key2 in shared_keys:
        if first_dict.get(key2) == second_dict.get(key2):
            diff_diff[key2] = {CONDITION: UNCHANGED, VALUE: first_dict[key2]}
        elif isinstance(second_dict.get(key2), dict) and isinstance(first_dict.get(key2), dict):  # noqa:E501
            diff_diff[key2] = {
                CONDITION: NESTED,
                VALUE: build_diff_tree(first_dict[key2], second_dict[key2]),
            }
        else:
            diff_diff[key2] = {
                CONDITION: CHANGED,
                VALUE: {
                    DELETED: first_dict[key2],
                    ADDED: second_dict[key2],
                },
            }
    for key3 in added_keys:
        diff_diff[key3] = {CONDITION: ADDED, VALUE: second_dict[key3]}
    return diff_diff
