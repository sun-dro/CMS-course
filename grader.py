"""
Library providing functions to automatically grade student homeworks.
"""

import doctest
import importlib
from os.path import abspath
from os.path import dirname
from os.path import join
from os.path import splitext
import subprocess
import sys
import unittest

HW_DIR = dirname(abspath(__file__))


def prepend_hw_path(filename, path=HW_DIR):
    """Prepend the homework's path in case the grader is called from outside."""
    return join(path, filename)

class TestCaseWithDoctests(unittest.TestCase):
    """Subclass this Test class if doctests should be checked."""
    def test_doctests(self):
        """Ensure doctests are present and pass."""
        module = importlib.import_module(splitext(self.target)[0])
        r = doctest.testmod(module)
        self.assertTrue(r.attempted, f'{self.target} does not have a doctest')
        self.assertFalse(r.failed, f'{self.target} contains failing doctests')


def grade_by_io(script, in_data, expected, points=1):
    """Grade a submitted example."""
    script = prepend_hw_path(script)
    process = subprocess.Popen(["python", script],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out, err = process.communicate(in_data.encode("utf-8"))
    actual = out.decode("utf-8")
    if expected.split() != actual.split():
        points = 0
    print(f'{points} points for {script}')
    if not points:
        if err:
            print("error:\n", err.decode('utf-8'))
        else:
            print("actual:\n", actual)
            print("expected:\n", expected)
    return points


def main():
    """Print error message telling students to call the individual graders instead."""
    print('library only for importing, call')
    print('python3 hw?_grader.py*')
    print('instead')


if __name__ == "__main__":
    sys.exit(main())
