'''
While creating file with 'x' mode, make sure file shouldn't be already exists.
'''
fh = open("../test_files/file1.txt", "xt")

# Writing into a file
fh.write("This file is created using 'x' mode in Python. \n")
fh.write("Next Line.")

# Closing the file. We can't perform any operations after closing the file
fh.close()