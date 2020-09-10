"""
CP1404 EMAILS
By Samantha Martin
Used solutions for assistance in this program as I was having issues
when I was splitting my email address.
"""

EMAIL_NAME = {}
email = input("Email: ")
before_at = email.split('@')[0]
parts = before_at.split('.')
name = " ".join(parts).title()
while email != "":
    confirmed_name = input("Is your name {}? (Y/n)".format(name))
    if confirmed_name.lower() != "y" and confirmed_name != "":
        name = input("Name: ")
    EMAIL_NAME[email] = name
    email = input("Email: ")

for email, name in EMAIL_NAME.items():
    print("{} ({})".format(name, email))