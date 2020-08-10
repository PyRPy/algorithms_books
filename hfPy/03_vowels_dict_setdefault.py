# Chapter 3 structured data
# dictionary
vowels = ['a', 'e', 'i', 'o', 'u']
word = "important"

found = {}
# use setdefault to avoid errors
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1 

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')