# 02_vowels.py
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
print('print all the vowels found: ')
for letter in word:
    if letter in vowels:
        print(letter)

# display unique vowels
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print('print vowels without duplicates: ')
for vowel in found:
    print(vowel)

# ask user to input words for searching
word = input('provide a word to search for vowels: ')
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print('print vowels in the word you input: ')
for vowel in found:
    print(vowel)