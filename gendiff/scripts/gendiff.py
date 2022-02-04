#!/usr/bin/env python3

from gendiff.args_parser import get_args
from gendiff.generate import generate_diff


def main():
    args = get_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
