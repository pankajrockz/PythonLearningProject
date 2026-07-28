#Tuple
# (item1, item2, ....., itemn)
# Sequence of items as a collection. Tuple elements cannot be update, added, deleted
# Tuples can also be initialized without paranetises like t1 = "Python", 10, 1.5, True, [1,2,4],(3,10)

t1=("Python", 10, 1.5, True, [1,2,4],(3,10))

#Accessing
print(t1)
print(type(t1))
print(t1[0])
print(type(t1[-2]))
print(t1[1:6])
print(t1[1:6:2])

#List to tuple and tuple to List
l1 = [1,2,3]
print(f"List: {l1}, Type: {type(l1)}")
t1=tuple(l1)
print(f"Tuple: {t1}, Type: {type(t1)}")
t2="apple", "grapes", "banana"
print(f"Tuple: {t2}, Type: {type(t2)}")
l2 = list(t2)
print(f"List: {l2}, Type: {type(l2)}")


