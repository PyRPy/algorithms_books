# logging_in.py
# step 1
import time
users = {}
status = ""

# step 3 
def newUser():
    createLogin = input("create a login name: ")
    if createLogin in users:
        print("\nLogin name already exists!\n")
    else:
        createPassw = input("create password: ")
        users[createLogin] = createPassw
        print("\nUser created!\n")
        logins = open("/Users/keli/Desktop/PythonDS/codingForPython/login.txt", "a")
        logins.write("\n" + createLogin + " " + createPassw)
        logins.close()

# step 4
def oldUsers():
    login = input("enter login name: ")
    passw = input("enter password: ")

    # check if user exists and login matches passwords
    if login in users and users[login] == passw:
        print("\nLogin sucessful!\n")
        print("User:", login, "accessed the system on:", time.asctime())
    else:
        print("\nUser doesn't exist or wrong password!\n")


# step 2
def mainMenu():
    global status 
    status = input("do you have a login account? y/n? or press q to quit")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    elif status == "q":
        quit()

mainMenu()
while status != "q":
    mainMenu()
