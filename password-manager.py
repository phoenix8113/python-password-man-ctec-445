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
        SelectionScreen(password)

def SelectionScreen(password):
    choice = int(input("Would you like to \n 1. Encrypt \n 2. Decrypt"))
    if choice == 1:
        encrypt(password)
    elif choice == 2:
        decrypt()
    else:
        print("Please select a valid option")

def encrypt(password):
    encryptPass = ''
    for i in password:
        if i.isalpha(): # Encrypt letters
            if i.isupper():
                encryptPass += chr((ord(i) + 3 - ord('A')) % 26 + ord('A')) #shifts the character; mod. 26 ensures it stays in the alphabet
            else:
                encryptPass += chr((ord(i) + 3 - ord('a')) % 26 + ord('a'))
        elif i.isdigit(): # Encrypt digits
            encryptPass += chr((ord(i) + 3 - ord('0')) % 10 + ord('0')) #shifts the character; mod. 10 ensures it stays in the numbers
    print("Original text:", password)
    print("Encrypted text:", encryptPass)

def bruteForceDecrypt(input_text):
    decrypted_result = ''
    for shift in range(1, 26):
        for char in input_text:
            if char.isalpha():
                if char.isupper():
                    decrypted_result += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
                else:
                    decrypted_result += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            elif char.isdigit():
                decrypted_result += chr((ord(char) - shift - ord('0')) % 10 + ord('0'))
            else:
                decrypted_result += char

        print("Shift +" + str(shift) + ": " + decrypted_result)
        decrypted_result = ''
def decrypt():
    encrypted_text = input("Enter encrypted text")
    shift = int(input("Enter the shift (Enter 0 to brute force) "))
    decrypted_result = ''
    if shift != 0:
        for i in encrypted_text:
            if i.isalpha():
                if i.isupper():
                    decrypted_result += chr((ord(i) - shift - ord('A')) % 26 + ord('A'))
                else:
                    decrypted_result += chr((ord(i) - shift - ord('a')) % 26 + ord('a'))
            elif i.isdigit():
                decrypted_result += chr((ord(i) - shift - ord('0')) % 10 + ord('0'))
            else:
                decrypted_result += i
        print(decrypted_result)
    else:
        bruteForceDecrypt(encrypted_text)



inputLength()