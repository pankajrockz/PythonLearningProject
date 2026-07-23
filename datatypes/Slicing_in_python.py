s1 = "Hello World"

"""
Syntax of indexing: string[index]
Syntax of Slicing: string[start:end:step]
- start: Slicing starting index
- end: Slicing ending index(where end element is excluded)
- step: Slicing step
print(s1)

#Length of a String
print(len(s1))

#Indexing
print("First character is: ", s1[0])
print("Last character is: ", s1[-1])
"""

# print(s1[1:11:2])
# print(s1[2:9:2])

s1_slice = s1[1:12:3]

print(s1_slice)
print(type(s1_slice))