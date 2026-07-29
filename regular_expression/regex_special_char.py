'''
Character pattern => [A-Z],[a-z]
One key points when matching a character pattern - In strings we can have some escape characters like 'old\new' string
will treat \n as new line hence regex might not work as per our pattern. So for character pattern matching we always
need to use 'r' before the string to tell python that treat this as a raw string. Ex pat = r"old\new"
'''
import re

# Matching first two consecutive lower case character
s1 = "Python is a programming language. python3.14 is the current version."
pat = r"[a-z][a-z]"
match_obj = re.search(pat, s1)
print(match_obj)
'''
Output: <re.Match object; span=(1, 3), match='yt'>
'''

# Matching set of characters having 1st upper case and remaining 2 lower case character
match_obj = re.search(r"[A-Z][a-z][a-z]", s1)
print(match_obj)
'''
Output: <re.Match object; span=(0, 3), match='Pyt'>
'''

'''
\d, \D
\d matches first digit character. it is similar to [0-9]
\D matches first any non digit character. 
'''
pat = r"[a-z][a-z][a-z]\d"
match_obj = re.search(pat, s1)
print(match_obj)
'''
Output: <re.Match object; span=(37, 41), match='hon3'>
'''

pat = r"[a-z][a-z][a-z]\D"
match_obj = re.search(pat, s1)
print(match_obj)

'''
\s, \S
\s - Matches any whitespace character
\S - Matcher any non whitespace character(space, \n and \t)
'''
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat, s1)
print(match_obj)
'''
Output: <re.Match object; span=(3, 7), match='hon '>
'''

s2 = """Hi there
We are learning_Python

"""
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat, s2)
print(match_obj)
'''
Output: <re.Match object; span=(5, 9), match='ere\n'>

\s also matches new line or a tab characters.
'''
pat = r"[a-z][a-z][a-z]\S"
match_obj = re.search(pat, s2)
print(match_obj)
'''
Output: <re.Match object; span=(3, 7), match='ther'>
'''

'''
\w, \W
\w - Is for alphanumeric character, basically it matches [A-Z], [a-z], [0-9], _(underscore)
\W - Its opposite of \w and matches character except [A-Z], [a-z], [0-9], _(underscore)
'''
pat = r"[a-z][a-z][a-z]\w"
match_obj = re.search(pat, s2)
print(match_obj)
'''
Output: <re.Match object; span=(3, 7), match='ther'>
'''

pat = r"[a-z][a-z][a-z]\W"
match_obj = re.search(pat, s2)
print(match_obj)
'''
Output: <re.Match object; span=(5, 9), match='ere\n'>
'''
