# filter(function, sequence) - Filter the elements from the sequence based on the function condition

seq = [1,2,3,4]
# odd = lambda x:True if x%2 != 0 else False
# filtered_output = filter(odd, seq)

# above can also be written like
filtered_output = filter(lambda x:True if x%2 !=0 else False, seq)
print(filtered_output) # This provides the output as a object
print(f'Odd numbers in the above sequence are: {list(filtered_output)}')

'''
Output: 
<filter object at 0x000001D646B35990>
Odd numbers in the above sequence are: [1, 3]
'''


#map(function, sequence) - Map object will be returned with the output of the function condition for the sequence

mapped_object = map(lambda x:True if x%2 !=0 else False, seq)
print(mapped_object)
print(f'Map Output: {list(mapped_object)}')
'''
Output: 
<map object at 0x000001D646B47DC0>
Map Output: [True, False, True, False]
'''

#For the above example, map is not the right way as it will only result True, False map. Rather the below example is the
# the best example of use of map where we want square of every element in the map
sq_map = map(lambda y: y ** 2, seq)
print(f'Square Map of list {seq} is: {list(sq_map)}')
'''
Output: 
Square Map of list [1, 2, 3, 4] is: [1, 4, 9, 16]
'''
