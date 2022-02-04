import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='First file to compare')
    parser.add_argument('second_file', type=str, help='Second file to compare')
    parser.add_argument('-f', '--format', choices=['json', 'plain', 'stylish'],
                        default='stylish',
                        help='set format of output. stylish is default')
    return parser.parse_args()