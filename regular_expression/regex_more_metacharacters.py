import re

s1 = "Python is a programming language"

# ^ - Carat - Exactly match in the beginning of the string
pat = r"^[A-Z][a-z]{5}"
match_obj = re.search(pat, s1)
print(match_obj)
'''
Output: <re.Match object; span=(0, 6), match='Python'>
'''

# $ - Exactly match at the ends with
pat = r"[a-z]{4}$"
match_obj = re.search(pat, s1)
print(match_obj)
'''
Output: <re.Match object; span=(28, 32), match='uage'>
'''

# group - () - Basically used to match the exact string
# or - | - Or operator is to add mutiple pattern if previous one is not matched it will look for this
emails = "abc_123@example.com random words and characters. x12y3.abc.edu"
pat = r"(com|edu)"
match_obj = re.search(pat, emails)
print(match_obj)
'''
Output: <re.Match object; span=(16, 19), match='com'>
'''
