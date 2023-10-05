# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.

def triple(x): 
    return x*3
x=4
result = triple(x) 
print(result)

# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
def subtract(a,b):
    x = a-b
    return x
result = subtract(5,2)
print(result)

# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
# You should program the function and not use
# the function "dict" directly
def dictionary_maker(tuple_list):
    dictionary = {}  
    for key, value in tuple_list:
        dictionary[key] = value  
    return dictionary

tuple_list = [('Ana', 25), ('Jose', 30)]

result = dictionary_maker(tuple_list)
print(result)

############################################
#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".