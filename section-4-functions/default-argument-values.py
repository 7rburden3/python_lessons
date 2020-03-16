def add(a = 0, b = 0):
    return a + b

print(add())
# here add uses the default arguments of 0
print(add(7, 8))
# here add uses the arguments we have provided for a and b
print(add(10))
# here add uses 10 as the argument for a and uses the default argument for b