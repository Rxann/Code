import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ123456789!$*^"

while 1:
    password_len = int(input("How many characters are needed? "))
    passwork_count = int(input("How many passwords should be generated? "))
    for x in range(0, passwork_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is you password: ", password)
        
            