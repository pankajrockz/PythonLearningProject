'''
Loop - Anytime we need to repeat a block of statement we use loop. In python we have two loops for and while loop
For loop is an iterator based loop which steps through the items of a collection (list, tuples, set, dict, str),
and executes a block of code repeatedly for a number of times equal to the items/elements of that collection
'''
from dictionary.dictionary_intro import groceries

#For loop with list
l = ['Mark', 10.2, 1980]
for i in l:
    print(f'{i}', end=", ")
print()

percents = [85.5, 81.0, 86.0, 83.5]
for percent in percents:
    print(f'{percent}', end=', ')
print()

#For loop with string
x='apple'
for i in x:
    print(f'{i}', end=', ')
print()

s1 = "Hello World"
for ch in s1:
    print(ch, end=", ")
print()

#for loop with range - Range is a builtin function used to generate sequence of integers in a given int
#Range syntax - range(start, stop, step) - Stop is not included in the generation
#range(start, stop) - step =1 by default
#range(stop) - start = 0, so range will have 0 -> stop-1
for i in range(1,11): #by default step is 1
    print(i, end=", ")
print()

#Reverse iteration
for i in range(20,10,-1):
    print(i, end=", ")
print()

#Countdown from 10 to 1(1 included)
for i in range(10,0,-1):
    print(i, end=", ")
print("Happy New Year!!!!")

#Iterate list with range
groceries = ['salt', 'milk', 'suger']
for i in range(len(groceries)):
    print(groceries[i], end=", ")
print()

profits = [9, 11, 6, 10]
for i in range(len(profits)):
    print(f'Profit of quater {i+1} is {profits[i]}')

#for loop with dict
employee = {"empId": 1001, 'name': 'Mark', 'dept':'HR'}
for emp in employee:
    print(emp, employee[emp])

#When using .items on dict which gives tuples
for emp in employee.items():
    print(emp)

#Max - Min - Sum

#Sum
scores = [2, 45, 102, 4, 9, 12, 45, 90, 1, 0, 1]
sum = 0
for score in scores:
    sum += score
# sum = sum(scores) - This is without loop and using inbuilt function.
print(f'Total run scored is {sum}')

#Max
highest_score = scores[0] # Assume the first value is highest
for score in scores:
    if score > highest_score:
        highest_score = score
# highest_score = max(scores) - This is without loop and using inbuilt function.
print(f'Highest run scored is {highest_score}')

#Min
minimum_score = scores[0] # Assume the first value is lowest
for score in scores:
    if score < minimum_score:
        minimum_score = score
# minimum_score = min(scores) - This is without loop and using inbuilt function.
print(f'Minimum run scored is {minimum_score}')