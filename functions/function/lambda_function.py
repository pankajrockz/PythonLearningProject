"""
Anonymous function or lambda function when function doesn't contain any name.
"""

def add(a):
    return a+1

print(add(2))
"""
#Syntax
lambda argument : expression
"""

fun = lambda a : a+1
res = fun(2)
print(res)

#Passing two argument in lambda
fun = lambda a,b : a+b
res = fun(2,6)
print(res)
