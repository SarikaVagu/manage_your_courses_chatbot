from StudentLogin import StudentMenu
import hashlib
import sys
import signal
import getpass
from users import Database
from adminmenu import adminMenu

db=Database()

def keyboardInterruptHandler():
    db.serializeDatabase()
    sys.exit(0)

def new_user_validate(username, password):
    if (username in db.getDatabase()):
        return False
    elif password != '':
        return True
    else:
        return False

def existing_user_validate(username , password):
    if (username in db.getDatabase()):
        if (password==db.getDatabase()[username]):
            return True
        else:
            return False
    else:
        return False

def isAdmin(username):
    return username=="Admin"

def login():
    print("____LOGIN____")
    global username
    username=input("Enter Username: ")
    password = hashlib.sha256(getpass.getpass(prompt='Enter Password: ', stream=None).encode()).hexdigest()
    if existing_user_validate(username,password):
        print("Login Succesful")
        if isAdmin(username):
            adminMenu()
        else:
            StudentMenu()
    else:
        print("Login Unsuccesful")
        mainMenu()
    
def SignUp():
    print("___SIGNUP____")
    username=input("Enter Username: ")
    password = getpass.getpass(prompt='Enter Password: ', stream=None)
    password = hashlib.sha256(password.encode()).hexdigest()
    
    # we will be storing boolean value for admin
    
    isAdmin=bool(input("Please choose account type:\n1.Admin\n2.Student\nEnter your choice: ")=='1')
    if new_user_validate(username,password):
        if (db.addUser(username, password, isAdmin)):
            print("User created successfully!")
        else:
            print("User creation unsuccessful")
        mainMenu()
    else:
        print("User creation unsuccesful")
        mainMenu()


def mainMenu():
    try: 
        print("1.Login  2.SignUp  3.Exit")
        choice=int(input())
        if choice==1:
            login()
        elif choice==2:
            SignUp()
        elif choice == 3:
            db.serializeDatabase()
            return
        else:
            print("please enter valid choice")
            mainMenu()
    except Exception as e:
        print(e)
        mainMenu()

    # previous code
    # try:
    #     print("1.Login 2.SignUp 3.Exit")
    #     choice=int(input())
    #     if choice==1:
    #         login()
    #     elif choice==2:
    #         SignUp()
    #     elif choice==3:
    #         return
    #     else:
    #         print("please enter valid choice")
    #         mainMenu()
    # except Exception as e:
    #     print("Please enter valid input")
    #     mainMenu()

print("Hey, I am your virtual assistant. I can help you with finding and registering courses")
signal.signal(signal.SIGINT, keyboardInterruptHandler)
mainMenu()