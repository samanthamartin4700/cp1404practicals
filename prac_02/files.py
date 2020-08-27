# 1.
# out_file = open("name.txt", "w")
# name = input("Please enter your name: ")
# print(name, file=out_file)
# out_file.close()

# 2
# in_file = open("name.txt", "r")
# file_contents = in_file.read()
# print("Your name is", file_contents)
# in_file.close()

# 3.
# in_file = open("numbers.txt", "r")
# first_number = int(in_file.readline())
# second_number = int(in_file.readline())
# total = first_number + second_number
# print(total)
# in_file.close()

# 4.
number= 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number += (int(line))
print(number)
in_file.close()