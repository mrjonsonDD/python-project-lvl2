#!/usr/bin/env python3


import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    args = parser.parse_args()
    print(args.indir)


if __name__ == '__main__':
    main()
