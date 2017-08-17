# file_variable = open('name.txt', 'w')
# username = input("please enter your name: ")
# print(username, file=file_variable)
# file_variable.close()


# file_variable = open('name.txt', 'r')
# username = file_variable.read()
# print("Your name is {}".format(username))
# file_variable.close()


file_variable = open('numbers.txt', 'r')
number_1 = int(file_variable.readline())
number_2 = int(file_variable.readline())
total_value = number_1 + number_2
print(total_value)
file_variable.close()


