"""
Goat Latin is a made-up language based off of English, sort of like Pig Latin.

The rules of Goat Latin are as follows:

1. If a word begins with a consonant (i.e. not a vowel), remove the first
letter and append it to the end, then add 'ma'.  For example, the word 'goat' becomes 'oatgma'.

2. If a word begins with a vowel (a, e, i, o, or u), append 'ma' to the end of the word.
For example, the word 'I' becomes 'Ima'.

3. Add one letter "a" to the end of each word per its word index in the
sentence, starting with 1. That is, the first word gets "a" added to the
end, the second word gets "aa" added to the end, the third word in the
sentence gets "aaa" added to the end, and so on.

Write a function that, given a string of English words making up one sentence, returns that
sentence in Goat Latin.

For example:

  string_to_goat_latin('I speak Goat Latin')

would return: 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
"I, speak , Goat Latin"
ord('a') < ord(c) < ord('z')
"""

def string_to_goat_latin(sentence):
  words = sentence.split ()
  vowels = ['a','e','i','o','u']
  new_words = []
  for idx in range(len(words)):
    word = words[idx]
    if not word.isalpha():
        continue
    if word[0].lower() in vowels:
      new_word = word+'ma'
    else:
      if len(word) < 2:
        new_word = word+'ma'
      else:
        new_word = word[1:]+word[0]+'ma'
    new_word +='a'*(idx+1)
    new_words.append(new_word)
  return ' '.join(new_words)

print (string_to_goat_latin('I speak B Goat Latin'))

"""
You are given a square grid of size N, where N>=3. I have placed a battleship
of size 3 somewhere in the grid, and you want to sink my battleship by
ordering the bombing of specified coordinates. The battleship can only be
placed vertically or horizontally, not diagonally.
Every coordinate which does not contain the battleship is empty.

Your task is to write the find_battleship function which takes N as input, and returns the 3 coordinates of the battleship.
Assume you have a function, boolean bomb_location(x, y), which will return True if (x, y) "hits" the battleship and False if (x, y) misses the battleship.

For example, in the following grid your function find_battleship(N),
given N of 8,  would return ((1,2), (2,2), (3,2)):

. . . . . . . .
. . X . . . . .
. . X . . . . .
. . X . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
"""


def find_battleship (N):

    res = []

    while r <= N and not stop:
        while l <= N and not stop:
            if bomb_location(r,c):
                res.append(r,c)
                if len(res) == 3:
                    stop = True
            l+=1
        r+=1

    return res
