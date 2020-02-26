print(type(5)) # invoke the type function
print(type(10)) # output tells us that these integers are of the class int

print(type(3.8)) # this time we create an instance object of the class float
print(type(5.0)) # this time we create an object of the class float

print(type("computer"))
print(type("laptop"))

print(type(5) == type(10)) # here we are using the boolean equals to see if the class (in this case two instances of the int class) are the same
print(type("computer") == type("laptop"))
print(type(5) == type(5.0))
print(type(5) == type("5"))

print(type(True)) # creates an instance of class Boolean
print(type(False)) # creates an instance of class Boolean
print(type(False) == type(True)) # returns True as this is a comparison of the Boolean class

print(type([1, 2, 3]))
print(type({"UK": "Edinburgh"}))