# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:15:23 2018

@author: Valentin
"""

import pandas as pd

data = pd.read_csv('lyrics.csv')

broilers = data[data['artist'] == 'beyonce-knowles']

broilers_lyrics = ''

for song in broilers['lyrics'].dropna():
     broilers_lyrics += song

broilers_lyrics = broilers_lyrics.replace(',', ' ,')
broilers_lyrics = broilers_lyrics.replace('.', ' .')
broilers_lyrics = broilers_lyrics.replace('?', ' ?')
broilers_lyrics = broilers_lyrics.replace('!', ' !')
broilers_lyrics = broilers_lyrics.replace('\'s', ' \'s')
broilers_lyrics = broilers_lyrics.replace('-', ' - ')
broilers_lyrics = broilers_lyrics.replace(u'\xad', ' - ')

with open('broilers_lyrics.txt','w',encoding='utf-8') as f:
    f.write(broilers_lyrics)
