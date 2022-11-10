#!/usr/bin/env python3

# Copyright (c) 2013 Gerald Senarclens de Grancy <oss@senarclens.eu>
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""
This program counts how many times each word in a given text file occurs.

The result is printed to the terminal.
"""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="Text file to be analyzed.")
    args = parser.parse_args()
    with open(args.infile, encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    count_unique(words)
    count_unique_sorted(words)


def count_unique(words):
    """
    Return a dictionary of unique words and the number of their occurence.

    Two words are considered the same only when they have exactly the same
    characters. However, the characters are not compared case sensitive.
    Eg. 'vaLuE' is considered the same as 'Value'.
    Also, some of the words still contain punctuation marks which have to be
    removed before comparison.

    `words` - a list of words
    """
    unique_words = {}
    new_list = []
    for word in words:
        new_list.append(word.lower().strip(',').strip('.'))
        new_list = ' '.join(new_list).split()
    for word_l in new_list:
        unique_words[word_l] = new_list.count(word_l) + 1

    return unique_words

def count_unique_sorted(words):
    """
    Return a list of named tuples containing the frequency of each word.

    The first element of each named tuple is 'word' and the second 'count'.
    The list has to contain the tuples in the same order as they occur in the
    argument.

    `words` - a list of words
    """
    dict_1 = count_unique(words)
    list_tuples = list(dict_1.items())
    return list_tuples


if __name__ == "__main__":
    sys.exit(main())
