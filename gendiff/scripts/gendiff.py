#!/usr/bin/env python3

import argparse
from gendiff.generate import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='First file to compare')
    parser.add_argument('second_file', type=str, help='Second file to compare')
    parser.add_argument('-f', '--format', choices=['json', 'plain', 'stylish'],
                        default='stylish',
                        help='set format of output. stylish is default')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
