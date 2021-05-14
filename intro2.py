greeting = "Hello there young one. welcome to narnia. what is your name?"


def the_intro():
    print(greeting)
    char_name = input("Please enter your name: ")
    welcome_greeting = print("It is nice to have you here " + char_name + ". Walk with me as i tell you a story")

def math_addition():
    x = input("Pls enter the first number to add: ")
    y = input("Pls enter the second number to add: ")
    z = x + y
    print("x + y = "+ z)
    print(type(z))

    math_addition()