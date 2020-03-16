# python is a dynamically typed language which means a variable does not need to have a type declared whenever it is written.

# create a function that takes a word and repeats it a set number of times

# def word_multiplier(word, times):
#     return word * times

# print(word_multiplier("dog", 5))

# we have not explicitly stated the variable types- python has recognised a string and an integer.
# Function annotations allow us to clarify what datatypes are expected for the parameters

def word_multiplier(word: str, times: int) -> str:
    # use colon to define datatype for parameters
    # use -> to define datatype of return value
    return word * times

print(word_multiplier("dog", 5))

# this is more for your own or others documentation as if we do:
print(word_multiplier(10, 5))
# the program doesn't crash but returns the value of 50