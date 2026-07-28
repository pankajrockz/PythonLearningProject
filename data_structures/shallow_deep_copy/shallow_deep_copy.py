import copy

#Shallow copy - duplicates the top-level structure of an object but shares references to any nested objects.
l1 = [1, 2.5, [10,20,30]]
l2 = copy.copy(l1)
print(l2)
print(id(l1))
print(id(l2))
print(id(l1[0]))
print(id(l2[0]))

d1 = {'id': 111, 'name':'John', 'marks':{'eng':71.5, 'math':91.5, 'bio':80.0}}
d2 = copy.copy(d1)
print(f'd1: {d1} having id: {id(d1)}')
print(f'd2: {d2} having id: {id(d2)}')

# As this is replacement of value, values will not be change
l1[0] = 10
d1['name'] = 'Mary'
print(f"l1: {l1} having id: {id(l1)}, l2: {l2} having id: {id(l2)}")
print(f"d1: {d1} having id: {id(d1)}, d2: {d2} having id: {id(d2)}")

# As this is modification in the list value have the same memory address, l2 values will also be changed
l1[-1][-1] = 300
d1['marks']['eng'] = 78.5
print(f"l1: {l1} having id: {id(l1)}, l2: {l2} having id: {id(l2)}")
print(f"d1: {d1} having id: {id(d1)}, d2: {d2} having id: {id(d2)}")

# Deep copy - recursively duplicates every object, creating a completely independent clone.
l3 = [1, 2.5, [10,20,30]]
d3 = {'id': 222, 'name':'Ram', 'marks':{'eng':61.5, 'math':81.5, 'bio':90.0}}
print(f"l3 values: {l3}, having id: {id(l3)}")
print(f"d3: {d3} having id: {id(d3)}")
l4 = copy.deepcopy(l3)
d4 = copy.deepcopy(d3)
print(f"l4 values: {l4}, having id: {id(l4)}")
print(f"d4: {d4} having id: {id(d4)}")

print(f'Id for l3[0]: {id(l3[0])}, \nId for l4[0]: {id(l4[0])}')
print(f'Id for d3[\'name\']:{id(d3['name'])}, \nId for d4[\'name\']:{id(d4['name'])}')

# As deepcopy create a completely new copy of list so it doesn't have any memory reference
l3[0] = 10
d3['name'] = 'Sita'
print(f"l3: {l3} having id: {id(l3)}, \nl4: {l4} having id: {id(l4)}")
print(f"d3: {d3} having id: {id(d3)}, \nd4: {d4} having id: {id(d4)}")

# As this modification is in the list l3 value, l4 values will not be changed
l3[-1][-1] = 300
d3['marks']['eng'] = 23.0
print(f"l3: {l3} having id: {id(l3)}, \nl4: {l4} having id: {id(l4)}")
print(f"d3: {d3} having id: {id(d3)}, \nd4: {d4} having id: {id(d4)}")