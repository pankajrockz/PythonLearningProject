# In dict when we have same keys with different values, the later value will be updated
student1_marks = {"maths": 80.5, "eng": 76.0, "physics": 76.0, "maths": 81.6}
print(student1_marks)

#get() - When we use get method to find a key value which is not present in dict it will return NONE and will not fail.
print(student1_marks.get("engs"))

#get() with default value if not present but it will not add the value into the dict. It return the value if key present
print(student1_marks.get("chem", 89.0))
print(student1_marks.get("eng", 89.0))
print(student1_marks)

#Membership Operator - In / Not In - This operator only works for key
print("maths" in student1_marks)
print(80.5 in student1_marks)

#Update the dict with other dict like concatenation. If the key is already present, values will be updated
sem1_marks = {"maths": 80.5, "eng": 76.0, "physics": 76.0}
sem2_marks = {"chem": 81.9, "bio": 74.6, "eng": 99.0}
sem1_marks.update(sem2_marks)
print(sem1_marks)

#Pop - Delete the key value pair from the dict
sem1_marks.pop("chem")
print(sem1_marks)

#In dict, not allowed keys - list, set, dict - Because these are mutable
#Allowed keys - int, str, float, boolean, tuple - Because these are immutable
#Keys of dict can only be immutable datatype
#d1 = {[1,2,3]:6} # Key as list Not allowed
# d2 = {{1,2,3}:6} # Key as set Not Allowed
# d2 = {{1:"One",2:"Two",3:"Three"}:6} # Key as dict Not Allowed

#Values - Can be any datatype
student1 = {'id': 1001, 'name': 'John', 'marks': [89.5, 71.5, 81.0]} # List as value
print(student1.get('marks'))
print(student1.get('marks')[-1])
student2 = {'id': 1001, 'name': 'John', 'marks': {'eng':89.5, 'chem':71.5, 'math':81.0}} # Dict as value
print(student2.get('marks'))
print(student2.get('marks').get('math'))

#Fetch only the keys, we can use keys()
print(student2.keys(),type(student2.keys()))

#Fetch only the values, we can use values()
print(student2.values(),type(student2.values()))

# items will be used when we need the key value pair
print(student2.items(),type(student2.items()))



