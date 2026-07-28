#os.path.exists() - Its part of os module. It can also check the directory is existing or not.

import os, pathlib
file_name = "practice.txt" # This even work with the full path if file is not present in the same directory.

if os.path.exists(file_name):
    print("File Exists!!!")
else:
    print("File not Exists!!!")

# pathlib.Path.exists() - We can use pathlib module.

file_name = pathlib.Path("practice.txt")
if file_name.exists():
    print("File Exists!")
else:
    print("File not exits, creating it...")
    fh=open(file_name, 'xt')
    fh.write("Some content")
    fh.close()