'''
a mode - Append mode to append the file
If file is not exists, it creates the file and then perform the write operations.
'''

fh = open("../test_files/practice.txt", "at")
fh.write("This content has been written using 'a' mode.\n")
fh.write("'a' mode is used to add new content at the end of the file.\n")
fh.write("Good Bye!")
fh.close()