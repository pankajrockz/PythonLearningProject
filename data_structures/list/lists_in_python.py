name = "John"
age = 23
percent = 85.5

student = [name, age, percent]
print(type(student))
print(student)
days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print(days_of_week)
print(days_of_week[0])
print(days_of_week[-7])

print(len(days_of_week))

#Slicing in List
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(li[1:6:1])
print(li[::2])

#Concatination
l2 = [11,12,13,14,15,16,17,18,19,20]
print(li+l2)
print(l2+li)

#Repetation
print(l2*3)

#Append

fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print(fruits)

#insert
fruits.insert(1, "Mango")
print(fruits)

#extends
fruits.extend(["Guava", "Blueberry"])
print(fruits)

#remove
fruits.remove("Blueberry")
print(fruits)
#fruits.remove("Blueberry") #When element doesn't exist, it will throw error
print(fruits)

#pop
fruits.pop() #This will delete the last value same as pop(-1)
print(fruits)

fruits.pop(2)
print(fruits)

#reverse
fruits.reverse()
print(fruits)

#sort
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

#Count
numbers = [1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 0, 9, 10, 0, 11, 0]
print(numbers.count(0))

#membership
print(0 in numbers)
print(100 in numbers)
print(100 not in numbers)

#Number operations on list
#min
print(min(numbers))

#max
print(max(numbers))

#Total
print(sum(numbers))

#nested list
l1 = [5, 1.5, "Python", True, None, [1,2,3], 10]
print(f"Length of list: {len(l1)}")
print(f"Second last element: {l1[-2]}")

#Fetching the element of the inner list
print(f"Inner list first element: {l1[-2][-1]}")

l2 = [[1,2], [3,4], [5,6,[0,1]]]
print(f"Inner list: {l2[-1][-1]}")
print(f"Inner list last element: {l2[-1][-1][-1]}")
