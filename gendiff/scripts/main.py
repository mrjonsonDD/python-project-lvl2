#!/usr/bin/env python3

from gendiff.difference import generate_diff
from gendiff.gendiff_engine import cli_parser


def main():
    arguments = cli_parser()
    diff = generate_diff(
        arguments.first_file, arguments.second_file, arguments.format)
    print(diff)


if __name__ == '__main__':
    main()
