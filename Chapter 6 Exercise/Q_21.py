"""An anagram of a word is a word that is created by rearranging the letters of the original.
For instance, two anagrams of idle are deli and lied. Finding anagrams that are real words is
beyond our reach until Chapter 12.

Instead, write a program that asks the user for a string
and returns a random anagram of the string—in other words, a random rearrangement of the
letters of that string."""

from random import shuffle
word = input('Enter a word: ')
new_word = list(word)
shuffle(new_word)
new_word_2 = ''.join(new_word)
print(new_word_2)
