print("Welcome to the V Buck Generator")
user = input("What is your Epic games user name: ")
Platform = input("What platform do you play on: ")
amnt = input("How many V Bucks would you like to be generated: ")
key = "vbuckgen"


print("Generating...")
print("verification passed :)")
print(f"Complete. We gave {user} on {Platform} {amnt} of V bucks")

print("You can find the key in the key.txt file :)")
attempt = input("Please enter the key if you would like more v bucks: ")
if attempt == key:
    vbuck_attempt_2 = input("How many extra v bucks would you like to be generated: ")
    print(f"Ok, We succesfully gave you {vbuck_attempt_2} v bucks to {user}")

print("Finished")
