import random
import secrets
import string

listAll = string.ascii_letters + string.digits


def GeneratePassword(length):  # function to generate password
    password = ''.join(secrets.choice(listAll) for i in range(length))  # borrowed from 'secrets' documentation
    ContainsTwoNumbers(password, length)  # calls function to ensure there are two numbers


def inputLength():  # function which allows the user to input their desired password length
    global length
    try:
        length = int(input("How many characters should your password be? "))  # Asks user for password length
    except:  # Error Handling; This is a broad except statement which needs to be further tested to ensure invalid number is the issue
        print("Please enter a valid number")
        inputLength()
    if length < 10:  # checks for  a length greater than 10 (as specified in the assignment instructions)
        print("Your password must be at least 10 characters long!")
        inputLength()
    else:
        GeneratePassword(length)  # proceeds to the generate password funtion with the user inputed length


def ContainsTwoNumbers(password, length):  # verifies the password generated contains two numbers
    num_count = 0
    for i in password:  # loops through the chars in password
        if i.isdigit():  # if the char is a digit
            num_count += 1
    if num_count < 2:
        print("Regenerating password...")
        GeneratePassword(length)  # regenerates the password if there is not 2 numbers
    else:
        print("Generated password:", ''.join(password))  # prints the generated password


inputLength()


'''
def SelectionScreen():
    choice = int(input("Would you like to \n 1. Encrypt \n 2. Decrypt"))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    else:
        print("Please select a valid option")
'''
