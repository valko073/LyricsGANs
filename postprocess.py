# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:15:23 2018

@author: Valentin, Mathis
"""

import re
from nltk.corpus import words

# import nltk
# nltk.download('words')


# pre-compile regex
apostrophe = re.compile(r'(\w) ([smt]\s|l{2}\s)', re.IGNORECASE)


# clean the lines
with open('./data/sample.txt', 'r', encoding='utf-8') as f:
    cleaned = ''
    for line in f.read().splitlines():
        if '`' not in line:
            line = re.sub(apostrophe, r"\1'\2", line)
            cleaned += line + '\n'
    with open('./data/sample_clean.txt', 'w', encoding='utf-8') as out:
        out.write(cleaned)


# select the good lines
with open('./data/sample_clean.txt', 'r', encoding='utf-8') as f:
    wordSet = set(words.words())
    selection = ''
    for line in f.read().splitlines():
        lineWords = line.split()
        if len(line) == 32:
            # line is overflowing => last word does not need to be a word
            lineWords = lineWords[:-1]
        accept = True
        for word in lineWords:
            if '\'' in word:
                # take the word before the '
                word = word[:word.index('\'')]
            if word not in wordSet:
                # check the dictionary
                accept = False
        if accept and len(line) > 3:
            # minimum of 3 characters
            if len(set(lineWords)) > len(lineWords) - 3:
                # maximum of 2 duplicate occurances of words
                selection += line + '\n'
    with open('./data/sample_selection.txt', 'w', encoding='utf-8') as out:
        out.write(selection)
