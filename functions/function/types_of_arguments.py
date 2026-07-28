# Positional Argument - Passing the argument in order of their position. All the arguments needs to be passed while
# calling the function.
def add(a, b):
    return a + b
result = add(10, 7) # so 10 will be assigned to a and 7 will be assigned to b

#Default Argument - Passing the default value of an argument if nothing is passed. Default argument can only be the
# assigned at the end while defining.
def add(a, b=5):
    return a + b
result = add(10, 10)
print(result)

result1 = add(10)
print(result1)

#Keyword Argument - If we need to only pass the one of the default argument we will use keyword argument
def add(a, b = 5, c = 10):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b +c
add(11, c=100)
add(c = 11, b = 20, a = 1)