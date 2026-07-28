# Mutability & Immutability
# Mutability means the ability of being updated. Like List
# Immutability means the ability od being not updated. Like tuple, string


s1 = "Python is fun"
s1.replace("Python","Java") # This will not update the s1, it just return the value.
print(s1)
s2 = s1.replace("Python","Java")
print(s2)

t1 = ("Mango", "Orange", "Apple")
#t1.append("Banana") #This will fail as append is not available in tuple.
print(t1)

l1 = list(t1)
print(id(l1))
l1.append("Banana")
print(l1)
print(id(l1)) # Same memory address after the append due to mutablity of list.

l1[-1] = "Blueberry"
print(l1)
print(id(l1))
print(id(l1[0]))
print(id(l1[1]))
print(id(l1[2]))
print(id(l1[3]))

