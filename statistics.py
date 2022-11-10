#!/usr/bin/env python3

"""
This module contains functions to compute the statistical values
of a given column in a given csv file.
"""

import argparse
import math
import sys


def items(filename):
    """Return one line at a time as dictionary.

    The first line has to be a header that can be used as dictionary keys. All
    numeric values in the input file are automatically converted to float.
    Calling this generator function again after the last line restarts at the
    top.
    """
    with open(filename, encoding='utf-8-sig') as f:
        header = [e.strip() for e in f.readline().split(',')]
        for line in f:
            if not line.strip():
                continue
            columns = line.split(',')
            item = dict(zip(header, columns))
            for key in item:
                try:
                    item[key] = float(item[key])
                except:
                    pass
            yield item


def count(filename):
    """Return the number of items in the given file."""
    num_items = 0
    for item in items(filename):
        num_items += 1
    return num_items


def calc_mean(filename, key):
    """
    """
    raise NotImplementedError


def calc_stddev(filename, key):
    """
    """
    raise NotImplementedError


def calc_sum(filename, key):
    """
    """
    raise NotImplementedError


def calc_variance(filename, key):
    """
    """
    raise NotImplementedError

def calc_median(filename, key):
    """
    """
    return NotImplementedError


def main():
    """
    Entry point if the module is started as designated program.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Text file to be analyzed.")
    parser.add_argument("key",
                        help="Name of the column that should be analyzed.")
    args = parser.parse_args()

    print("count:\n", count(args.filename))
    print("sum:", calc_sum(args.filename, args.key))
    print("mean:", calc_mean(args.filename, args.key))
    print("variance:", calc_variance(args.filename, args.key))
    print("standard deviation:", calc_stddev(args.filename, args.key))
    print("median:", calc_median(args.filename, args.key))

if __name__ == "__main__":
    sys.exit(main())
