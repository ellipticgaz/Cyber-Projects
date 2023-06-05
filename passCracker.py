# This programme uses a brute force method to crack passwords entered by user.

import random

# List of potential characters.
characters = "0123456789!@#$%^&*()_+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
character__list = list(characters)
# User input password.
password = input("enter password: ")
# Guess user password.
guess_password = ''
while (guess_password!=password):
    guess_password = random.choices(character__list, k=len(password))
    print(">>>>>"+str(guess_password)+"<<<<<")
    if (guess_password==list(password)):
        print("Your password is:" +"".join(guess_password))
        break


