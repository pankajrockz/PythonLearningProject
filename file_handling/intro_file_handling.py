'''
Here we will see how to handle files in python.
In python, files get classified in two ways
1. Text Files - Here data stored in form of characters, like name of emp, salary of emp, etc
2. Binary Files - Here data stored in form of bites(group of 8 bytes), like audio or video files.

To do any operation on file, we need to open a file. To open a file in python will use open function
open(file_name, mode_to_open)
Modes:
1. r - Read
2. x - Create
3. w - Write or overwrite
4. a - Append
5. t - Text mode
6. b - Binary file
'''

file_handler = open("../test_files/practice.txt", 'rt')
print(file_handler)

#Read Operation
# read() => It read the contents of the file as str. It will read all the content of the file
'''
content = file_handler.read()
print(content, type(content))
'''

# If we need to only read certain number of characters => read(number_of_characters)
'''
content1 = file_handler.read(10)
print(content1, type(content1))
'''

# If we need to read line from the file we'll use the readline() function. Every readline call will read the next line
'''
read_line1 = file_handler.readline()
read_line2 = file_handler.readline()
read_line3 = file_handler.readline()
read_line4 = file_handler.readline()

print(f'Line 1: {read_line1}')
print(f'Line 2: {read_line2}')
print(f'Line 3: {read_line3}')
print(f'Line 4: {read_line4}')
'''

# readlines() - To read all the lines and store it in the list.

all_lines = file_handler.readlines()
print(f'All lines are: {all_lines}')

for line in all_lines:
    print(line.rstrip('\n')) # It will remove the \n from the right of the each line

# Closing a file after opening to free up the space.
file_handler.close()



