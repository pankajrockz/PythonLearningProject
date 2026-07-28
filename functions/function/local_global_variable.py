n = 1 # Global Variable

def fn():
    global n # When using global keyword, it updates the global variable inside the function
    n = 5 # Local Variable
    print('in', n)

fn()

print('out', n)