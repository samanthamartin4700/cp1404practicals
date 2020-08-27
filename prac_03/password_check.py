password = input("Enter password (minimum 8 characters): ")
while len(password) < 8:
    print("Incorrect password. Your password must be more than 8 characters long!")
    password = input("Enter password (minimum 8 characters): ")
print("*" * len(password))