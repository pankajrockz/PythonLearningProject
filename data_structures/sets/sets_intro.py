# Sets are non-sequential collection of items
# comma separated element enclosed within {}
# Cannot have indexing and slicing
# Sets elements are immutable but set is mutable as it has add, remove, clear methods.
# Set cannot have duplicate elements
# Sets are unordered

set1 = {10,"Python", 2.5}
print(set1)

#This will fail
# set[0] = 1

# Length
print(len(set1))

# Sets can't have duplicates but list and tuple can
l1 = [10, 2.5, 10, 30, 10]
print(l1, type(l1))
s1 = {10, 2.5, 10, 30, 10}
print(s1, type(s1))


