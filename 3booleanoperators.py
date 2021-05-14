import getpass

def check_boolean():
    print(10 > 9)
    print(10 == 9)
    print(10 < 9)
#check_boolean()

def boolean_condition():
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")
    if username == "admin" and password == "ninjacoder":
        print("Welcome nerd. you have entered Nerd Inc.")
    else:
        print("your username and password are incorrect.")
        try_again = input("would you like to try again? y or n")
        if try_again == "y":
            boolean_condition()
        else:
            print("have a good day, you ain't allowed into Nerd Inc.")
boolean_condition()
