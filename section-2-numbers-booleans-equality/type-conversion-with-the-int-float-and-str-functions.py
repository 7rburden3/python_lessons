print(int(3.14)) # this is not rounding, it is simply cutting off the decimal point
print(int(3.99)) # this also returns an output of 3
print(int("3")) # invoking the int function so taking the string object and trying to return an int object
print(int(3))

print(float(5))
print(float("10.32"))
print(float(5.23))

print(str(5.35)) # invoke string function will return a string object of its argument
print(str(5))
print(str("Hello"))

# print(5 + "Hello") will return an error as trying to concatenate an int and a string

print(str(5) + " Hello") # this will work as the int is being converted to a string

print(5 + int("5"))

print(3 + 5.8) # python automatically converts the int to a float ie it becomes print(float(3) + 5.8)
# this is known as a "mixed type expression" as it contains two different types.

print(str(5) + " 5")

print(int("1000"))

print("$" + str(99.45) + " dollars")

print(9 % 4)