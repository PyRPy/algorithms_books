# head first python 
# chapter 2
word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("take one down")
    print("pass it around")
    if beer_num == 1:
        print("no more bettles of beer on the wall.")
    else:
        if beer_num - 1 == 1:
            word = "bottle"
        print(beer_num - 1, word, "of beer on the wall.")
    print()
