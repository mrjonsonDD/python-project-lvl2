import argparse


def generate_diff():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output\
                        (default: stylish)')
    return parser.parse_args()
