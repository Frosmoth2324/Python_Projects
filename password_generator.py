import random
import string


def gen_pass(min_length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special
    print()
    print(pwd)



while True:
    dig = input("How many characters should the password be? ")
    if dig.isdigit():
        dig = int(dig)
        if dig > 0:
            break
        else:
            print("Password length must be greater than zero")
    else:
        print("Please enter a digit")
while True:
    print("Do you want numbers? [y/n] ")
    num = input()
    if num == "y":
        num = True
        break
    elif num == "n":
        num = False
        break
while True:
    print("Do you want special characters? [y/n] ")
    spec = input()
    if spec == "y":
        spec = True
        break
    elif spec == "n":
        spec = False
        break
gen_pass(dig, num, spec)