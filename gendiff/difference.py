#!/usr/bin/env python3

from gendiff.file_reader import get_format, get_content
from gendiff.parser_data import parser
from gendiff.formatters.get_format import select_formatter
from gendiff.diff_tree import build_diff_tree


def prepare_content(data_path):
    data_format = get_format(data_path)
    data = get_content(data_path)
    return parser(data_format)(data)


def generate_diff(data1, data2, output_format='stylish'):
    dict1 = prepare_content(data1)
    dict2 = prepare_content(data2)
    diff = build_diff_tree(dict1, dict2)
    return select_formatter(diff, output_format)
