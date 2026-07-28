nums = { 1, 3, 2, 0, -1}

#Membership Operations - In/Not IN
print(0 in nums)
print(1 not in nums)

#Concatination is not allowed in Sets set1 + set2

#Repetation is not allowed in sets. S1*3

#Type Casting tuple to Set
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
weekday = set(weekdays)
print(weekday) #Orders will be changed as set is unordered collection of items

#Set is mutable
s1= {2, 0, -1}
print(s1)

#Add
s1.add(5)
s1.add(5)
print(s1)

#Remove
s1.remove(0)
print(s1)

#Discard - As remove fails if element is not available and we try to remove,
# but discard doesn't fail even if element is not present which we are trying to remove.
s1.discard(0)
print(s1)

#Clear
s1.clear()
print(s1)

#Common between two sets - Intersection and `&` can be used
student1 = {"English", "Math", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics"}
common_subjects = student1.intersection(student2)
common_subjects2 = student1 & student2
print(common_subjects)
print(common_subjects2)

#Union - All subject - We can used union and `|` operator
student3 = {"Sanskrit", "Math", "CS"}
all_subjects = student1.union(student2, student3)
all_subjects2 = student1 | student2 | student3
print(all_subjects)
print(all_subjects2)

# Difference between two sets can be achived with difference method and `-` operator
days = {"Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"}
weekends = {"Sat", "Sun"}
weekdays = days - weekends
print(weekdays)
weekdays = days.difference(weekends)
print(weekdays)

# Frozen sets - Immutable Sets
fs1 = frozenset({10,20,30})
print(fs1, type(fs1))
fs2 = frozenset({10,50,100, 200})

#Frozensets can have intersection, union, difference, Non Unique
print(fs1 & fs2)
print(fs1 | fs2)
print(fs1 - fs2)
print(fs1 ^ fs2)
