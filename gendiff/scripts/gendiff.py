#!/usr/bin/env python3
import argparse
from gendiff.constants import JSON, PLAIN, STYLISH
from gendiff.gendiff_engine import generate_diff


def main():
    """Print difference of two file."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        choices=[JSON, PLAIN, STYLISH],
        default=STYLISH,
        help='set format of output. stylish is default format',
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
