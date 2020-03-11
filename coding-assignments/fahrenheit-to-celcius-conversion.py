# The Challenge
# Design a Python program that asks the user for a temperature in Fahrenheit.

# The program should convert the temperature to Celsius and print out a message with the value.

# When dealing with any numeric values in this problem, prefer floating point values to integers.

# Fahrenheit to Celsius Formula
# Subtract 32 from the Fahrenheit temperature.

# Multiply the result by (5 / 9).

# Example:

# 100 Fahrenheit

# 100 - 32 = 68

# 68 multiplied by (5 / 9) is 37.77

# 37.77 Celsius

fahr_num = float(input("Please enter the temperature in Fahrenheit: "))

cels_num = str(round(((fahr_num - 32) * (5 / 9)), 2))

print("The temperature in Celsius is:", cels_num + " C")

# ds solution

# user_value = input("Enter a temperature in Fahrenheit to convert to Celsius ")
# fahr_temp = float(user_value)
# cels_temp = (fahr_temp - 32) * (5/9)
# print(fahr_temp, "in Celsius is", cels_temp)