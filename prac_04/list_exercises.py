# NUMBER = 5
# numbers = []
# for number in range(1, NUMBER + 1):
#     choice = int(input("Number: "))
#     numbers.append(choice)
#
# print("The first number is {}".format(numbers[0]))
# print("The last number is {}".format(numbers[-1]))
# print("The smallest number is {}".format(min(numbers[:])))
# print("The largest number is {}".format(max(numbers[:])))
# print("The average of the numbers is {}".format((sum(numbers[:])) / len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username: ")
if username in usernames:
    print("Access denied")
else:
    print("Access granted")