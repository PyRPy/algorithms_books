# Chapter 3 structured data
# use set for the solution

vowels = set('aeiou')
word = "important"
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)