a = None
print(type(a))

def subtract(a, b):
    print(a - b)
    # here nothing is being explicitly returned

result = subtract(5, 3)
print(result)
#this will return None as in the subtract function we are not explicitly requiring a return statement