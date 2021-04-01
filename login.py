login_correct_user = "rxan"
login_correct_pass = "8001"

login_user = input("What is the access name: ")
login_pass = input("What is the password: ")
name = input("What is you name: ")

if login_correct_pass and login_correct_pass == login_user and login_pass:
        print(f"Welcome {name}")
        print("Permission Granted")
        print("Nothing has been stored for now")
       
        
