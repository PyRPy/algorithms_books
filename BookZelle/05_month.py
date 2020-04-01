# 05_month.py
# how to extrat strings...as you want

def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = int(input("enter a month number (1-12): "))
    pos = (n - 1) * 3  # map to month abbrev
    monthAbbrev = months[pos : pos + 3] # slice it accordingly
    print("the month abbreviation is", monthAbbrev + ".")

main()