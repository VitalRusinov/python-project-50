"""Command line interface for gendiff."""

import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument(
        '-f', '--format',
        help='output format (default: stylish)',
        default='stylish',
        choices=['stylish']
    )
    return parser.parse_args()