import random

def gen_pass(pass_length):

    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    pass_length = int(input("Enter the length of password: "))

    password = ""
    for i in range(pass_length):
        password += random.choice(elements)

    return("your new password is :", password)    
