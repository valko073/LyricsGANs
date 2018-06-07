# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:15:23 2018

@author: Valentin, Mathis
"""

import pandas as pd
import re

# load all lyrics
data = pd.read_csv('./data/lyrics.csv')

# pre-compile regex
apostrophe = re.compile(r'(\w)\'([smt]|l{2}\s)', re.IGNORECASE)
punctuation = re.compile(r'([^\s])([-!?,.])', re.IGNORECASE)
single_word_brackets = re.compile(r'\n[\([][\w\-]+(\s\d+)?:?[\]\)]\s*\n', re.IGNORECASE)  # [Pre-Hook]
single_word_colon = re.compile(r'\n[\w\-]+(\s\d+)?:\s*\n', re.IGNORECASE)  # Verse 4:
short_lines = re.compile(r'\n+(.{0,10}\n)', re.IGNORECASE)  # lines up to 10 chars
special_char = re.compile(r'[^\w\s]', re.IGNORECASE)  # !IMPORTANT: removes umlaut
empty_lines = re.compile(r'\n\s*\n', re.IGNORECASE)
spaces = re.compile(r'  +', re.IGNORECASE)

# every artist
for artist in data.artist.unique():
    # save all lyrics into one string
    artist_lyrics = ''
    # get rows of artist
    songs = data[data.artist == artist]
    # only continue if we have at least x songs with lyrics
    if len(songs.lyrics.dropna()) > 50:
        for song in songs.lyrics.dropna():
            artist_lyrics += song + '\n'
        # clean the lyrics
        artist_lyrics = re.sub(apostrophe, r"\1 '\2", artist_lyrics)
        artist_lyrics = re.sub(punctuation, r"\1 \2", artist_lyrics)
        artist_lyrics = re.sub(single_word_brackets, '\n', artist_lyrics)
        artist_lyrics = re.sub(single_word_colon, '\n', artist_lyrics)
        # Otional steps:
        # take out all special characters
        artist_lyrics = re.sub(special_char, '', artist_lyrics)  # !IMPORTANT: removes umlaut
        # merge all short lines with the line above
        artist_lyrics = re.sub(short_lines, r' \1', artist_lyrics)
        # remove any empty lines
        artist_lyrics = re.sub(empty_lines, '\n', artist_lyrics)
        artist_lyrics = re.sub(spaces, ' ', artist_lyrics)
        # everything to lowercase
        artist_lyrics = artist_lyrics.lower()
        # save the lyrics
        if len(artist_lyrics.splitlines()) > 1000:
            with open('./data/preprocessed/' + artist + '.txt', 'w', encoding='utf-8') as f:
                f.write(artist_lyrics)
