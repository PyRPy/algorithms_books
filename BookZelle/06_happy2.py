# 06_happy.py
# improvement for shorter codes

def happy():
    return "Happy birthday to you!\n"

def verseFor(person):
    lyrics = happy()*2 + "Happy birthday, dear " + person + ".\n" + happy() 
    return lyrics 

def main():
    for person in ["Fred", "Lucy", "Elmer"]:
        print(verseFor(person))
        
main()
