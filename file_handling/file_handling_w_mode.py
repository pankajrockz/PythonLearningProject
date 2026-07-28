"""
w mode - Opens the file for writing. It helps to truncate/overwrites the file.
If file exists, it overwrites the content of the file
if file doesn't exist, it will create a new file and write the data.
"""

fh = open("../test_files/file2.txt", "wt")
fh.write("This file is overwritten using 'w' mode in Python. \n")
fh.write("Have a nice day!")
fh.close()