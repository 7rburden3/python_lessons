def p(text):
    print(text)
    # text is the parameter. When we call the function p() whatever argument we put inside the parantheses will be printed by the function p

p("Hello")
p("3")

# p()
# this will cause a TypeError which will explain how many arguments are missing - in this instance the error will tell us that p() is missing 1 required postional argument: 'text'

def add(a, b):
    print("The sum of", a, "and", b, "is", a + b)

add(3, 5)
add(-4, 7)

# again, giving add() the wrong number of arguments will result in errors appearing eg:

# add() gives a TypeError: add() missing 2 required positional arguments: 'a' and 'b'
# add(1) gives a TypeError: add() missing 1 required positional argument: 'b'
# add(3, 5, 7) gives a TypeError: add() takes 2 positional arguments but 3 were given