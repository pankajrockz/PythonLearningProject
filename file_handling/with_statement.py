"""
with statement - This statement get used to handle the files safely. Basically it simplifies resource management by
automatically handling the setup and clean up task. It ensures the resources are properly released even though there are
errors in the code.
"""

# fh = open("../test_files/practice.txt", "rt")

# Reading file using with statement
with open("../test_files/practice.txt", "rt") as fh:
    contents = fh.read()

print(contents)

# Creating a file using with statement and 'xt' mode
with open("../test_files/practice_1.txt", "xt") as fh:
    fh.write("New file creation\n")
    fh.write("Bye!!!")