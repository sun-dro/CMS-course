#!/usr/bin/env python3

import collections
import importlib  # TODO facture out to grader lib
import io
import os
import re
import sys
import unittest

from faker import Faker
import numpy as np

# TODO: remove after Python 3.6+ is in widespread use
try:
    ModuleNotFoundError
except NameError:
    ModuleNotFoundError = ImportError


SKEL_NO_SCRIPTS = """<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>Test</title>
<!-- Copyright (c) 2013 Tester. All rights reserved. -->
<meta equiv="content-type" content="text/html; charset=utf-8" />
<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
</head>
<body>

</body>
</html>
"""

SKEL_SCRIPTS = """<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>Test</title>
<!-- Copyright (c) 2013 Tester. All rights reserved. -->
<meta equiv="content-type" content="text/html; charset=utf-8" />
<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
<script src="js/test.js" type="text/javascript"></script>
<script src="js/other.js" type="text/javascript"></script>
<link rel="stylesheet" type="text/css" media="all" href="style.css" />
</head>
<body>

</body>
</html>
"""


class TestTelephoneNumbers(unittest.TestCase):
    target = "telephone_numbers.py"
    points = 1

    def test_lower(self):
        self.assertEqual(telephone_numbers.as_numeric('0800 reimann'),
                         '0800 7346266')

    def test_mixed(self):
        self.assertEqual(telephone_numbers.as_numeric('0699 GeraldS'),
                         '0699 4372537')

    def test_upper(self):
        self.assertEqual(telephone_numbers.as_numeric('0316 UNIGRAZ'),
                         '0316 8644729')


#class TestMakeHtmlSkeleton(unittest.TestCase):
    #target = "make_html_skeleton.py"
    #points = 2

    #def test_string_removal(self):
        #self.assertNotIn("description", make_html_skeleton.HTML_TEMPLATE)
        #self.assertNotIn("keyword", make_html_skeleton.HTML_TEMPLATE)

    #def test_string_addition(self):
        #new = ('<script src="http://code.jquery.com/jquery-1.10.1.min.js">'
               #'</script>')
        #self.assertIn(new, make_html_skeleton.HTML_TEMPLATE)

    #def test_make_html_skeleton_no_scripts(self):
        #filename = 'tmp.html'
        #make_html_skeleton.make_html_skeleton(year='2013',
                                              #name='Tester',
                                              #title='Test',
                                              #stylesheet=None,
                                              #filename=filename,
                                              #scripts=[])
        #with open(filename, encoding='utf-8') as f:
            #content = f.read()
        #self.maxDiff = None
        #self.assertEqual(content, SKEL_NO_SCRIPTS)
        #os.remove(filename)

    #def test_make_html_skeleton_scripts(self):
        #filename = 'tmp.html'
        #make_html_skeleton.make_html_skeleton(year='2013',
                                              #name='Tester',
                                              #title='Test',
                                              #stylesheet='style.css',
                                              #filename=filename,
                                              #scripts=['js/test.js',
                                                       #'js/other.js'])
        #with open(filename, encoding='utf-8') as f:
            #content = f.read()
        #self.maxDiff = None
        #self.assertEqual(content, SKEL_SCRIPTS)
        #os.remove(filename)

class TestFakeNewsGenerator(unittest.TestCase):
    target = "fake_news_generator.py"
    points = 2

    def test_female_credit(self):
        actual = fake_news_generator.fake_news(fake_news_generator.WORD_LIST,
                                               seed=1)
        self.assertEqual(actual, 'According to Sarah Gallagher hard exoneration long poll. Hard thank devaluation it’s.\nAt raising interest McCabe, committed 50\% long.')

    def test_word_list(self):
        seed = 0
        article = 'Presidency of Barack Obama'
        stdout = sys.stdout
        sio = io.StringIO()
        sys.stdout = sio
        argv = sys.argv
        sys.argv = sys.argv + ['--article', 'Presidency of Barack Obama',
                               '--seed', str(seed)]
        fake_news_generator.main()
        actual = sio.getvalue().strip()
        sys.argv = argv
        sys.stdout = stdout
        print(actual)
        actual = actual.translate({ord(' '): '', ord('.'): '', ord('\''): ''})
        self.assertFalse(re.search(r'\W+', actual),
                         'found characters that should be removed ("cleaned")')

        #fake = Faker('en_US')
        ## ungodly implementation of seed is not reliable when importing
        ## from other modules etc. wasted lots of time
        #fake.seed(seed)
        #person = fake.name_female()
        #words = wp.page(article).content.split()
        #word_list = fake_news_generator.clean_words(words)
        #max_chars = fake_news_generator.MAX_CHARS - len(person) - 1
        #text = fake.text(max_nb_chars=max_chars, ext_word_list=word_list)
        #expected = 'According to {} {}'.format(person,
                                               #text[0].lower() + text[1:])
        #self.assertEqual(actual, expected)
        #'According to Tina Kelly leadership that and '
                         #'obamas. Passage partnership of embargoed called cut '
                         #'on.')


class TestStatistics(unittest.TestCase):
    target = "statistics.py"
    points = 2
    filename = 'opesf.csv'

    @classmethod
    def setUpClass(cls):
        cls._open_values = []
        cls._volume_values = []
        with open(TestStatistics.filename, encoding='utf-8') as f:
            f.readline()
            for line in f:
                line = line.split(',')
                cls._open_values.append(float(line[1].strip()))
                cls._volume_values.append(float(line[-1].strip()))

    def test_calc_mean(self):
        actual = statistics.calc_mean(TestStatistics.filename, 'Open')
        self.assertAlmostEqual(actual, np.mean(TestStatistics._open_values))
        actual = statistics.calc_mean(TestStatistics.filename, 'Volume')
        self.assertAlmostEqual(actual, np.mean(TestStatistics._volume_values))

    def test_calc_stddev(self):
        actual = statistics.calc_stddev(TestStatistics.filename, 'Open')
        self.assertAlmostEqual(actual, np.std(TestStatistics._open_values))
        actual = statistics.calc_stddev(TestStatistics.filename, 'Volume')
        self.assertAlmostEqual(actual, np.std(TestStatistics._volume_values))

    def test_calc_sum(self):
        actual = statistics.calc_sum(TestStatistics.filename, 'Open')
        self.assertAlmostEqual(actual, sum(TestStatistics._open_values))
        actual = statistics.calc_sum(TestStatistics.filename, 'Volume')
        self.assertAlmostEqual(actual, sum(TestStatistics._volume_values))

    def test_calc_variance(self):
        actual = statistics.calc_variance(TestStatistics.filename, 'Open')
        self.assertAlmostEqual(actual, np.var(TestStatistics._open_values))
        actual = statistics.calc_variance(TestStatistics.filename, 'Volume')
        self.assertAlmostEqual(actual, np.var(TestStatistics._volume_values))

    def test_find_max(self):
        actual = statistics.find_max(TestStatistics.filename, 'Open')
        self.assertAlmostEqual(actual, max(TestStatistics._open_values))
        actual = statistics.find_max(TestStatistics.filename, 'Volume')
        self.assertAlmostEqual(actual, max(TestStatistics._volume_values))

    def test_find_min(self):
        actual = statistics.find_min(TestStatistics.filename, 'Open')
        self.assertAlmostEqual(actual, min(TestStatistics._open_values))
        actual = statistics.find_min(TestStatistics.filename, 'Volume')
        self.assertAlmostEqual(actual, min(TestStatistics._volume_values))

    def test_calc_median(self):
        actual = statistics.calc_median(TestStatistics.filename, 'Open')
        self.assertAlmostEqual(actual, np.median(TestStatistics._open_values))
        actual = statistics.calc_median(TestStatistics.filename, 'Volume')
        self.assertAlmostEqual(actual, np.median(TestStatistics._volume_values))


class TestCountUnique(unittest.TestCase):
    target = "unique_words.py"
    points = 4

    def test_empty(self):
        self.assertEqual(unique_words.count_unique([]), {})

    def test_count_lower(self):
        with open("text", encoding="utf-8") as f:
            text = f.read().lower()
        words = text.split()
        expected = {"design": 3,
                    "develop": 2,
                    "maintain": 1,
                    "and": 6,
                    "test": 2,
                    "cloud": 4,
                    "applications": 2,
                    "in": 3,
                    "python": 3,
                    "document": 3,
                    "api": 2,
                    "for": 3,
                    "services": 3}
        self.assertDictEqual(unique_words.count_unique(words), expected)

    def test_count(self):
        with open("text", encoding="utf-8") as f:
            text = f.read()
        words = text.split()
        expected = {"design": 3,
                    "develop": 2,
                    "maintain": 1,
                    "and": 6,
                    "test": 2,
                    "cloud": 4,
                    "applications": 2,
                    "in": 3,
                    "python": 3,
                    "document": 3,
                    "api": 2,
                    "for": 3,
                    "services": 3}
        self.assertDictEqual(unique_words.count_unique(words), expected)

    def test_count_sorted(self):
        with open("text", encoding="utf-8") as f:
            text = f.read()
        words = text.split()
        Pair = collections.namedtuple('Pair', ['word', 'count'])
        expected = [Pair("design", 3),
                    Pair("develop", 2),
                    Pair("maintain", 1),
                    Pair("and", 6),
                    Pair("test", 2),
                    Pair("cloud", 4),
                    Pair("applications", 2),
                    Pair("in", 3),
                    Pair("python", 3),
                    Pair("document", 3),
                    Pair("api", 2),
                    Pair("for", 3),
                    Pair("services", 3)]
        self.assertEqual(unique_words.count_unique_sorted(words), expected)


def grader(result):
    """Return the number of points obtained by the result"""
    total = result.testsRun
    successes = total - len(result.errors) - len(result.failures)
    points = successes / total * result.points
    print(points, "points for", result.target)
    return points

if __name__ == "__main__":
    tests = (TestTelephoneNumbers,
             #TestMakeHtmlSkeleton,
             TestFakeNewsGenerator,
             TestStatistics,
             TestCountUnique)
    total = 0.0
    thismodule = sys.modules[__name__]
    for test in tests:
        module = test.target.split('.')[0]
        try:
            setattr(thismodule, module, importlib.import_module(module))
        except ModuleNotFoundError as e:
            #print(test.target, 'not found; 0 points')
            print(test.target, 'import error; 0 points')
            print(e)
            continue
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test)
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        result.target = test.target
        result.points = test.points
        total += grader(result)
    print()
    print(total, "points in total")
