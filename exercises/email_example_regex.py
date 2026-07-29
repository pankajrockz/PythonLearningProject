import re

pattern = r"\b[a-zA-Z]+[\w.-]+@[a-z]+[.][a-z]+\b"
c_pattern = re.compile(pattern)

with open("../test_files/student_details.txt", "rt") as fh:
    data = fh.read()

match_obj = re.finditer(c_pattern, data)

for match in match_obj:
    print(match)