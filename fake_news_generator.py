#!/usr/bin/env python3

"""
Simple fake news generator with commandline interface.
"""

import argparse
import re
import sys

from faker import Faker
import wikipedia as wp

MAX_CHARS = 140  # limit from twitter

TWEET1 = ['Russia', 'and', 'China', 'are', 'playing', 'the', 'currency',
    'devaluation', 'game', 'as', 'the', 'U.S.', 'keeps', 'raising', 'interest',
    'rates', 'Not acceptable!']
TWEET2 = ['Comey', 'drafted', 'crooked', 'Hillary', 'exoneration', 'long',
          'before', 'he', 'talked', 'to', 'her', '(lied in Congress)', 'then',
          'based', 'his', 'decisions', 'on', 'her', 'poll', 'numbers',
          'disgruntled', 'he', 'McCabe,', 'and', 'the', 'others',
          'committed', 'many', 'crimes', ]
TWEET3 = ['just', 'hit', '50\%', 'in', 'the', 'Rasmussen', 'poll', 'much',
          'higher', 'than', 'President Obama', 'at', 'same', 'point', 'with',
          'all', 'of', 'the', 'phony', 'stories', 'and', 'Fake', 'News,',
          'it’s', 'hard', 'to', 'believe', 'thank', 'you', 'America,', 'we',
          'are', 'doing', 'great', 'things']
# sorting is needed to ensure random seed produces reliable outcome
WORD_LIST = sorted(set(TWEET1) | set(TWEET2) | set(TWEET3))


def clean_words(word_list):
    """Return given word_list with only alphanumeric chars or the '_'."""
    pattern = re.compile('[\W_]+')
    word_list = set(word_list)
    return sorted([pattern.sub('', word).lower() for word in word_list])


def fake_news(word_list, seed=None):
    """Generate fake news to be tweeted."""
    fake = Faker('en_US')
    if seed:
        Faker.seed(seed)
    person = fake.name()
    text = fake.text(max_nb_chars=MAX_CHARS - len(person) - 1,
                     ext_word_list=word_list)
    return 'According to {} {}'.format(person, text[0].lower() + text[1:])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--article',
                        help='use article from English wikipedia for wordlist')
    parser.add_argument('--seed', help='use seed for faker module')
    args = parser.parse_args()
    if args.article:
        word_list = wp.page(args.article).content.split()
    else:
        word_list = WORD_LIST
    seed = args.seed or None

    print(fake_news(word_list, seed))


if __name__ == "__main__":
    sys.exit(main())
