'''
Regex metacharacters are special symbols that do not match themselves literally; instead, they dictate how the pattern -
matching engine processes text. They act as the programmatic instructions within a regular expression.
'''

import re

message =  "The current Python version is 3.14. Other previous versions are 3.13, 3.12, 3.11"

# First any consecutive digits
match_obj = re.search("[0-9][0-9]", message)
print(match_obj)
'''
Output: <re.Match object; span=(32, 34), match='14'>
'''

match_obj = re.search("[0-9][0-9]", "House no: 251/A")
print(match_obj)
'''
Output: <re.Match object; span=(10, 12), match='25'>
'''

match_obj = re.search("[0-9][0-9][0-9]", "House no: 251/A")
print(match_obj)
'''
Output: <re.Match object; span=(10, 13), match='251'>
'''

# . => Dot matches any characters except new line character(\n). If we want to match the dot(.), we need to add it in
# square bracket like [0-9][.][0-9][0-9]
match_obj = re.search("[0-9].[0-9][0-9]", message)
print(match_obj)
'''
Output: <re.Match object; span=(30, 34), match='3.14'>
'''

match_obj = re.search("[0-9].[0-9]", message)
print(match_obj)
'''
Output: <re.Match object; span=(30, 33), match='3.1'>
'''

match_obj = re.search("[0-9].[0-9][0-9]", "The year is 2011")
print(match_obj)
'''
Output: <re.Match object; span=(12, 16), match='2011'>
'''

