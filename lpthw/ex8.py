formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter, formatter, formatter, formatter)
print(formatter.format(
        "try your",
        "own text here",
        "maybe a peom",
        "or or a song about fear"
))
