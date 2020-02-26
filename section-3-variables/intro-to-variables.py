name = "Ralph" # name is variable, object is string Ralph
age = 46 # age is variable, object is int 46
handsome = True
favourite_language = "Python"

print(name) # returns Ralph
print(handsome)
# print(occupation) will not work as occupation is not defined

print(age + 4) # will return 50
print("My name is", name, "and I am", age, "years old")

age = 23
print(age) #program is running sequentially so whilst it sees the first age as 46, when it gets to here, it sees that the variable age has now changed to 23

age = 23 + 10 
print(age) # what takes place to the right of the equals sign always occurs first.

fact_or_fiction = 6 < 10
print(fact_or_fiction) # will return True as the above line is a Boolean and 6 is less than 10

chameleon = 5
print(chameleon)

chameleon = "Some string"
print(chameleon)

chameleon = 5.55
print(chameleon)

chameleon = False
print(chameleon)
