'''
There will be an issue where we can't able to access the data as a dictionary after writing the data into the text file,
hence we require the pickle module to use to store the file contents and access it back. Pickle module has couple of
functions that is used for putting the datatypes like dict, list and tuple in a file and function to read and access back
the data. Tuple works with binary data where basically serialization(converting the text data to binary) and
deserialization(converting the binary data back to text) happen. Let's first look at the issue which we will face when
trying to do the same operation directly working with text file.

students = {'student1':{'roll':101, 'name': 'Mark', 'percent':98.5, 'sports': True},
            'student2':{'roll':102, 'name': 'Joe', 'percent':89.7, 'sports': False},
            'student3':{'roll':103, 'name': 'Carol', 'percent':77.3, 'sports': True}}
print(students, type(students), sep='\n')

with open("../test_files/students_data1.txt", wt) as fh:
    fh.write(str(students)) # We can't directly pass dictionary to write() as it accepts only string hence typecasted

with open("../test_files/students_data1.txt", rt) as fh:
    for student in fh:
        print(student) # This will read the data but as a string only

    content = fh.read() # This will read the data but as a string only, and we can't typecast string to dictionary
'''
import pickle

students = {'student1':{'roll':101, 'name': 'Mark', 'percent':98.5, 'sports': True},
            'student2':{'roll':102, 'name': 'Joe', 'percent':89.7, 'sports': False},
            'student3':{'roll':103, 'name': 'Carol', 'percent':77.3, 'sports': True}}

# Serialization
with open("../../test_files/students.bin", 'bw') as fh:
    for student in students:
        pickle.dump(students[student], fh)

# Deserialization
with open("../../test_files/students.bin", 'br') as fh:
    # If we know how many lines we can write as many pickle.load() but if add extra load it will fail with EOFError
    # print(pickle.load(fh))
    # print(pickle.load(fh))
    # print(pickle.load(fh))
    student_with_good_marks = []
    # When we don't know how many lines we have in the binary file, we need to use error handling
    while True:
        try:
            data = pickle.load(fh)
            print(data, type(data))
            # If we need to access any specific data we can use data['key]
            if data['percent'] >= 80:
                student_with_good_marks.append(data['name'])
        except EOFError as err:
            print("Done!!!")
            break

print(f'Students with marks greater then 80 are: {student_with_good_marks}')
