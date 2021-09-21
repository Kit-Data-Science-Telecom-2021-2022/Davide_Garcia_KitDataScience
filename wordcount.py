#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

# Function that create the dictionary and counting the occurrences
def counting_words(filename):
  word_dictionary= dict()  # defining the dictionary counting the words
  with open(filename, 'r') as file:
    for file_line in file:
      line = file_line.split()  # splitting the whole text into lines
      for element in line:
        element = element.lower()  # convert to lower case
        # checking if the word is already present in the dictionary
        if not element in word_dictionary:
          word_dictionary[element] = 1  # counting the first occurrence of the word
        else:
          word_dictionary[element] = 1 + word_dictionary[element]  # otherwise the counter is incremented
  # Checking if the file is closed
  if file.closed == False:
    print('The file is open')
  else:
    print('The file is closed')
  return word_dictionary

# Function printing the words sorted by words
def print_words(filename):
  word_dictionary = counting_words(filename)  # retrieve the dictionary
  word_dictionary = sorted(word_dictionary.items())  # sorting the dictionary by words

  for key, value in word_dictionary:  # printing the key and the value
    print(key, value)
  return

# Function printing the first 20 most repeated words
def print_top(filename):
  word_dictionary = counting_words(filename)  # retrieve the dictionary
  sorted_dict = sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True)  # sorting by the number of repetition
  sorted_dict = sorted_dict[:20]  # taking only the first 20 words
  for el in sorted_dict:  # printing the results
    print(el[0], el[1])
  return

###
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
