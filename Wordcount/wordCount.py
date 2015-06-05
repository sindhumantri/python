#! /usr/bin/python

import os

# open the file  
fp = open('wordCountExample.txt')
# read the file into text
text = fp.read()
# get the list of words (delimited-by space character)
words = text.split(' ')
# dictionary has key: word value: count
dict = {}
for word in words:
  # skip empty words
  if word != '':
    if not word in dict.keys():
      # first time entry
      dict[word] = 1
    else:
      # increment the value(count) if word exists in the dictionary
      dict[word] += 1
# looping the dictionary(dict)
for key in dict.keys():
  # printing key(word), value(count)
  print key, dict[key]

