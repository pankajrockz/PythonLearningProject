import json

students = {'student1':{'roll':101, 'name': 'Mark', 'percent':98.5, 'sports': True},
            'student2':{'roll':102, 'name': 'Joe', 'percent':89.7, 'sports': False},
            'student3':{'roll':103, 'name': 'Carol', 'percent':77.3, 'sports': True}}
print(students, type(students))

'''
To write the dictionary data in json we will dump() function of json module.
json.dump(dict, fileHandleObject, indent=4)
dict - Dictionary of data which we need to push to the file
fileHandleObject - File handling object to open the file
indent - To format the json file in readable format. Value of this will be number of spaces before the child elements
'''
with open("../../test_files/students_data.json", "w") as fh:
    json.dump(students, fh, indent=4)

'''
To read the data from the json we will use the load() function of json module.
json.load(fileHandleObject)
fileHandleObject - File handling object to open the file
'''
with open("../../test_files/students_data.json", 'r') as fh:
    data = json.load(fh)

print(data, type(data), sep='\n')

'''
To update the data to the json we will use the update() function of json module.
data.update(updated_data)
data - This is the actual data that we have to read first from the json file
updated_data - Updated data which we want to update into the json file

Steps of updating the json file:
1. Reading the old data from the json file and storing it into the variable
2. Updating the variable where we have stored the existing data
3. Dump the updated data variable to json file
'''
students_updated = {'student1':{'roll':111, 'name': 'Mark', 'percent':98.5, 'sports': False},
            'student2':{'roll':112, 'name': 'Joe', 'percent':22.7, 'sports': False},
            'student3':{'roll':113, 'name': 'Carol Lee', 'percent':32.3, 'sports': True}}

# Reading data
with open("../../test_files/students_data.json", 'r') as fh:
    data = json.load(fh)

# Updating data variable
data.update(students_updated)

# Dumping the updated data variable into the json file
with open("../../test_files/students_data.json", 'w') as fh:
    json.dump(data, fh, indent=4)