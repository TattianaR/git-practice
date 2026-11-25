#Password Length Checker.

password = input("Enter a password: ")
print("Password length is: ", len(password))

if len(password) >= 8:
    print("Password accepted.")
else:
    print("Password too short.")



