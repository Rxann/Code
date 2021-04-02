login_try = input("What is the access key: ")
keys = "6054"
if keys == login_try:
        print("Granted")
        print("mission succesfull")
        print("All information has been granted above")
if login_try != keys:
        print("Access denied. Please restart the program and try again")