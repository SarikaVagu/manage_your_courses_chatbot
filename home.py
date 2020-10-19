from StudentLogin import StudentMenu

def new_user_validate(user):
    return True

def existing_user_validate(user):
    return True

def isAdmin(regno):
    return False

def login():
    print("____LOGIN____")
    global regno
    regno=input("Enter RegisterNumber: ")
    password=input("Enter Password: ")
    if existing_user_validate([regno,password]):
        print("Login Succesful")
        if isAdmin(regno):
            # adminMenu()
            pass
        else:
            StudentMenu()
    else:
        print("Login Unsuccesful")
        mainMenu()
    
def SignUp():
    print("___SIGNUP____")
    regno=input("Enter RegisterNumber: ")
    password=input("Enter Password: ")
    # we will be storing boolean value for admin
    admin=bool(input("Please choose account type:\n1.Admin\n2.Student\nEnter your choice: "))
    if new_user_validate([regno,password,admin]):
        print("SignUp succesful\nPlease login to continue")
        login()
    else:
        print("Sign Up unsuccesful")
        mainMenu()


def mainMenu():
    try:
        print("1.Login 2.SignUp 3.Exit")
        choice=int(input())
        if choice==1:
            login()
        elif choice==2:
            SignUp()
        elif choice==3:
            return
        else:
            print("please enter valid choice")
            mainMenu()
    except Exception as e:
        print("Please enter valid input")
        mainMenu()

print("Hey, I am your virtual assistant. I can help you with finding and registering courses")
mainMenu()