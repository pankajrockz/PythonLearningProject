'''
Read Mode: r
1. When the provided file doesn't exist, it will throw the error
2. When opening a file with read mode 'rt' and try to write, it will throw the error. We can only use read() or readlines()
3.
'''
fh = open("../test_files/practice.txt", "rt")
content = fh.read()
fh.close()

print(content)

'''
Write Mode: a, w
1. When we try to read the file with write modes, it will throw the error
2. When using w mode, it will truncate the file if it exists or create new file if the file doesn't exists
'''

'''
Create Mode: x
1. When we try to create file which is already existing, it will throw the error
2. 

'''