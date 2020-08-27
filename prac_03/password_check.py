def main():
    password = get_password()
    show_asterix(password)


def show_asterix(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password (minimum 8 characters): ")
    while len(password) < 8:
        print("Incorrect password. Your password must be more than 8 characters long!")
        password = input("Enter password (minimum 8 characters): ")
    return password


main()