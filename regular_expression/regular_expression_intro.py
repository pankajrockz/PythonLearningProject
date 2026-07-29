'''
Regular Expression(RegEx)- Regular expressions (regex) are special text strings used for pattern matching, data
validation, and text searching and replacing. They provide a short way to find specific rules or shapes in large blocks
of words and numbers. Regular expression matching can be achieved with 're' module.

Syntax:
re.search(regex_pattern, string) => returns a match object(<class 're.Match'>) when there is a match, else return None

Output Format:
<re.Match object; span=(x, y), match='matchString'>
span=(x, y) => It tells the matching indexes where x is the starting point and y-1 is ending. y itself is not included.
match='matchString' => It tells about what string exactly matched i.e. matchString, for which the indexes given in span.
'''
import re

message =  "The current Python version is 3.14. Other previous versions are 3.13, 3.12, 3.11"

# If Python presents in the string
print("Python" in message)
print("14" in message)
print("13" in message)

print(message.find("Python"))
print(message.find("3.14"))


# Simple search using regular expression
match_obj = re.search('14', message)
print(match_obj, type(match_obj))
print(message[32:34])
'''
Output:
<re.Match object; span=(32, 34), match='14'> <class 're.Match'>
'''

if re.search('14', message):
    print("Found!!!")
else:
    print("Not Found!!!")
