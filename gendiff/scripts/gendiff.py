#!/usr/bin/env python3

from gendiff.diff_tree import build_diff_tree
from gendiff.gendiff_engine import generate_diff


def main():
    arguments = generate_diff()
    diff = build_diff_tree(
        arguments.first_file, arguments.second_file, arguments.format)
    print(diff)


if __name__ == '__main__':
    main()
