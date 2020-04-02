# 06_happy.py
def happy():
    print("happy birthday to you!")

def sing(person):
    happy()
    happy()
    print("happy birthday, dear", person + ".")
    happy() 

def main():
    sing("Fred")
    print()
    sing("Lucy")
    print()
    sing("Elmer")

main()
