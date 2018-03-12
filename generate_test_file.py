#!/usr/bin/env python

"""
Helper script that will generate a file composed of random characters to be
parsed by another program.
"""

import argparse
import random
import string

DEFAULT_FILE_LENGTH = 4096

def parse_args():
    """Parse Args"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-o',
                        '--output',
                        help='File to output to')
    parser.add_argument('--length',
                        default=DEFAULT_FILE_LENGTH,
                        help='Lenght of the file')
    args = parser.parse_args()
    return args

def get_character_list():
    """Get a list of chars used to generate random characters"""
    chars = []
    chars.extend(list(string.digits))
    chars.extend(list(string.letters))
    chars.extend(list(string.whitespace))
    return chars

def generate_random_characters():
    """Yields random characters"""
    chars = get_character_list()
    while True:
        yield random.choice(chars)

def main():
    """Main"""
    args = parse_args()
    file_length = int(args.length)
    random_chars = generate_random_characters()
    with open(args.output, 'wb') as fil:
        for _ in range(file_length):
            char = next(random_chars)
            fil.write(char)
        

if __name__ == "__main__":
    main()
