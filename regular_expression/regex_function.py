import re
from typing import cast

# match() - It will look for pattern at the beginning of the string

s1 = "We are learning regex in Python"
pat = r"[A-Z][a-z]"
match_obj = re.match(pat, s1)
print(match_obj)
'''
Output: <re.Match object; span=(0, 2), match='We'>
'''

pat = r"[a-z]{3}"
match_obj = re.match(pat, s1)
print(match_obj)
'''
Output: None
'''

#findall() - This will provide the list of all the matches
phones = "John-1234567890, Carol-9087654321, Mark-8970654321, Alice-38372882, Kailong-8273645362712345678"
pat = r"[0-9]{10}"
match_obj = re.findall(pat, phones)
print(match_obj)
'''
Output: ['1234567890', '9087654321', '8970654321', '8273645362']
'''

pat = r"[0-9]{7,15}"
match_obj = re.findall(pat, phones)
print(match_obj)
'''
Output: ['1234567890', '9087654321', '8970654321', '38372882', '827364536271234']
'''

#\b - Boundary value to match only if it exactly matches
pat = r"\b[0-9]{7,15}\b"
match_obj = re.findall(pat, phones)
print(match_obj)
'''
Output: ['1234567890', '9087654321', '8970654321', '38372882']
'''

# finditer - It will return all the matches in iterable so we can loop and read the matches
pat = r"\b[0-9]{7,15}\b"
match_obj = re.finditer(pat, phones)
for matches in match_obj:
    print(matches)
'''
Output: 
<re.Match object; span=(5, 15), match='1234567890'>
<re.Match object; span=(23, 33), match='9087654321'>
<re.Match object; span=(40, 50), match='8970654321'>
<re.Match object; span=(58, 66), match='38372882'>
'''

# sub() - Is used to substitute a pattern with another string or substring

s2 = "Sunday, Monday, Tuesday, Monday, Sunday, Saturday"
pat = r"Sunday"
replacement = "Friday"

# It will replace all the Sunday to Friday
result = re.sub(pat,replacement, s2)
print(result)
'''
Output: Friday, Monday, Tuesday, Monday, Friday, Saturday
'''

# It will replace only 1st Sunday to Friday due to count
result = re.sub(pat, replacement, s2, count=1)
print(result)
'''
Output: Friday, Monday, Tuesday, Monday, Sunday, Saturday
'''

pat = r"S[a-z]+"
result = re.sub(pat,replacement, s2)
print(result)
'''
Output: Friday, Monday, Tuesday, Monday, Friday, Friday
'''

message = """We are learning re. Using RE, we can search for a pattern in a given string.
Using the sub(), we can replace the pattern with a given string as well."""

pat = r"\bre\b"
replacement = "Regular Expression"
result = re.sub(pat, replacement, message, flags=re.IGNORECASE)
print(result)
'''
Output: We are learning Regular Expression. Using Regular Expression, we can search for a pattern in a given string.
Using the sub(), we can replace the pattern with a given string as well.
'''

phone_nums = "+91-2928383743, +91-9876745362"
pattern = r"[+-]"
replacement = ""
result = re.sub(pattern, replacement, phone_nums)
print(result)
'''
Output: 912928383743, 919876745362
'''

# compile()
phones = "John-1234567890, Carol-9087654321, Mark-8970654321, Alice-38372882, Kailong-8273645362712345678"
pattern = r"\d{10}"

# When we basically use basic pattern, re compiles it to create a compiled Pattern which then get internally used to
# find the matches. So when working on a project where we need to reuse these pattern again and again, its better to
# use the compiled pattern so for every match search it shouldn't run compile again.
c_pattern = re.compile(pattern)
print(c_pattern, type(c_pattern))

match_obj = re.findall(c_pattern,phones)
print(match_obj)
'''
Output: re.compile('\\d{10}') <class 're.Pattern'>
['1234567890', '9087654321', '8970654321', '8273645362']
'''

# Now lets use the above created compiled pattern in another match so it optimized the matches
with open("../test_files/student_details.txt", "rt") as fh:
    data = fh.read()
match_obj = re.findall(c_pattern,data)
print(match_obj)
'''
Output: ['9876543210', '1234567890', '5647382910']
'''
