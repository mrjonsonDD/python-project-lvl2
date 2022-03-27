#!/usr/bin/env python3
from gendiff.file_reader import get_format, get_content
from gendiff.parser_data import parser
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


def prepare_content(data_path):
    data_format = get_format(data_path)
    data = get_content(data_path)
    return parser(data_format)(data)


def generate_diff(data1, data2, output_format='stylish'):
    dict1 = prepare_content(data1)
    dict2 = prepare_content(data2)
    diff = build_diff_tree(dict1, dict2)
    return select_formatter(diff, output_format)


def build_diff_tree(dict1, dict2):
    result = {}
    set1 = set(dict1)
    set2 = set(dict2)
    com_keys = set1 & set2
    add_keys = set2 - set1
    dell_keys = set1 - set2
    for add_key in add_keys:
        result[add_key] = {
            TYPE: ADDED,
            VALUE: dict2.get(add_key)
        }

    for dell_key in dell_keys:
        result[dell_key] = {
            TYPE: REMOVED,
            VALUE: dict1.get(dell_key)
        }

    for com_key in com_keys:
        elem1 = dict1.get(com_key)
        elem2 = dict2.get(com_key)
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

        if elem1 == elem2:
            result[com_key] = {
                TYPE: UNCHANGED,
                VALUE: elem1
            }

    sorted_result = dict(sorted(result.items(), key=lambda k: k))
    return sorted_result
