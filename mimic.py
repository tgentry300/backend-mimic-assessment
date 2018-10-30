#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys
import string
import pprint

def read_file(file):
    with open(file, 'r') as file:
        file_lines = file.read().lower()
        file_list_no_punctuation =  file_lines.translate(None, string.punctuation).split()
    return file_list_no_punctuation


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    list_of_words = read_file(filename)
    mimic_dict = {}
    for i, word in enumerate(list_of_words):
        if word not in mimic_dict:
            mimic_dict[word] = [list_of_words[i + 1]]
        else:
            if i + 1 < len(list_of_words):
                mimic_dict.get(word).append(list_of_words[i + 1])
    return mimic_dict



def print_mimic(mimic_dict, start_word):
    """Given mimic dict and start word, prints 200 random words. Removed second argument as it is not needed for my implementation"""
    sentence = ''
    sentence += start_word
    for i in range(200):
        new_sentence = sentence.split()
        random_choice = random.choice(mimic_dict.get(new_sentence[-1]))
        sentence += ' ' + random_choice
    print sentence
        

    


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print 'usage: python mimic.py file-to-read'
        sys.exit(1)

    d = mimic_dict(sys.argv[1])
    start_word = 'then'
    print_mimic(d, start_word)


if __name__ == '__main__':
    main()
