# def add(a, b):
#     print("The sum of", a, "and", b, "is", a + b)

# add(4, 6)

# # this is a positional argument as the arguments are based on their position within the function

# add(a = 4, b = 6)

# # this is a keyword argument as we are specifically defining what a and b are

# add(b = 6, a = 4)

# # this provides the same answer as the invokation of the function above

def add(a, b, c):
    print("The sum of the three numbers is", a + b + c)

add(5, 10, 15)
add(a = 5, b = 10, c = 15)
add(5, b = 10, c = 15)

# add(10, a = 10, c = 15)
# this will NOT work, parameters must be in order when mxing and matching positional and keyword arguments

add(5, c = 15, b = 10)