# input("Enter some text: ") 
# at this point the program is still running
# print("I'll only print when you're finished typing.") 
# program is now finished

first_name = input("Please enter your first name: ")
print("It's nice to meet you,", first_name)

# Prompt the user for two numbers, one at a time
# The numbers will be received as strings
# Convert both numbers to integers
# Print a message that includes the sum of the two numbers

first_num = input("Please enter your first number: ")
second_num = input("Please enter your second number: ")

print("Hi", first_name + "!", "The sum of your two numbers is", (int(first_num) + int(second_num)))

# ds solution
# print("Let me help you add 2 numbers")
# first_input = input("Enter your first number! ")
# first_number = int(first_input)
# second_input = input("Enter your second number! ")
# second_number = int(second_input)
# print("The total is", first_number + second_number)

# ds solution cleaned up
# print("Let me help you add 2 numbers")
# first_number = int(input("Enter your first number! "))
# second_number = int(input("Enter your second number! "))
# print("The total is", first_number + second_number)