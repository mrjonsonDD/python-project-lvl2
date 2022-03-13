#!/usr/bin/env python3
from collections import OrderedDict
from gendiff.parser_file import prepare_file
from gendiff.formatters.get_format import select_formatter
from gendiff.constants import (
    ADDED,
    UPDATED,
    REMOVED,
    UNCHANGED,
    NESTED,
    TYPE,
    VALUE,
    OLD_VAL,
    NEW_VAL,
    CHILDREN
)


def generate_diff(path_file1, path_file2, output_format='stylish'):
    old_file = prepare_file(path_file1)
    new_file = prepare_file(path_file2)
    diff = build_diff_tree(old_file, new_file)
    return select_formatter(diff, output_format)


def build_diff_tree(old_file, new_file):
    result = {}
    set1 = set(old_file)
    set2 = set(new_file)
    com_keys = set1 & set2
    add_keys = set2 - set1
    dell_keys = set1 - set2
    for add_key in add_keys:
        result[add_key] = {
            TYPE: ADDED,
            VALUE: new_file.get(add_key)
        }

    for dell_key in dell_keys:
        result[dell_key] = {
            TYPE: REMOVED,
            VALUE: old_file.get(dell_key)
        }

    for com_key in com_keys:
        elem1 = old_file.get(com_key)
        elem2 = new_file.get(com_key)
        if elem1 == elem2:
            result[com_key] = {
                TYPE: UNCHANGED,
                VALUE: elem1
            }
        else:
            if isinstance(elem1, dict) and isinstance(elem2, dict):
                result[com_key] = {
                    TYPE: NESTED,
                    CHILDREN: build_diff_tree(elem1, elem2)
                }
            else:
                result[com_key] = {
                    TYPE: UPDATED,
                    OLD_VAL: elem1,
                    NEW_VAL: elem2
                }

    sorted_result = OrderedDict(sorted(result.items(), key=lambda k: k))
    return sorted_result
