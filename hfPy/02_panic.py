phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)

print(len(plist))

for i in range(4):
    print(plist.pop())
print(plist.pop(0))

plist.remove("'")
print(plist)

plist.extend([plist.pop(), plist.pop()])
print(plist)
plist.insert(2, plist.pop(3))
print(plist)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

paranoid_android = "Marvin"
letters = list(paranoid_android)
for char in letters:
    print('\t', char)
print()

paranoid_android = "marvin, the paranoid android"
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char)
print()
for char in letters[-7:]:
    print('\t'*2, char)
print()
for char in letters[12:20]:
    print('\t'*3, char)
