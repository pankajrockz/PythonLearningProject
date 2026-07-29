'''
Regex quantifiers specify how many times a preceding character or group must occur. By default, they are greedy,
matching as much as possible. Add ? to make them lazy/reluctant (matching as little as possible), or + for possessive
(matching all and never giving back to backtrack).

Standard Quantifiers
1. *: Matches 0 or more times. (e.g., a* matches "a", "aa", or an empty string).
2. +: Matches 1 or more times. (e.g., a+ matches "a", "aa" but not an empty string).
3. ?: Matches 0 or 1 time (makes the element optional). (e.g., colou?r matches both "color" and "colour").

Exact Quantifiers (Curly Braces)
1. {n}: Matches exactly n occurrences. (e.g., \d{3} matches exactly 3 digits).
2. {n,}: Matches at least n occurrences. (e.g., \d{3,} matches 3 or more digits).
3. {n,m}: Matches between n and m occurrences, inclusive. (e.g., \d{3,5} matches 3, 4, or 5 digits).

Advanced Modifiers
1. Lazy (Non-Greedy): Append ? to a quantifier (e.g., *?, +?, ??, {n,m}?) to force the engine to match the shortest
possible string.
2. Possessive: Append + to a quantifier (e.g., *+, ++, ?+, {n,m}+) to force the engine to consume as much as possible
and permanently lock the characters, preventing the engine from "giving back" to find a match.
'''

import re

message =  "The current Python version is 3.14. Other previous versions are 3.13, 3.12, 3.11"

# Standard Quantifiers
pat = r"[A-Z][a-z]*"
match_obj = re.search(pat, message)
print(match_obj)
'''
Output: <re.Match object; span=(0, 3), match='The'>
'''

pat = r"[A-Z][a-z]+"
match_obj = re.search(pat, message)
print(match_obj)
'''
Output: <re.Match object; span=(0, 3), match='The'>
'''

pat = r"[A-Z][a-z]?"
match_obj = re.search(pat, message)
print(match_obj)
'''
Output: <re.Match object; span=(0, 2), match='Th'>
'''

# Exact Quantifiers (Curly Braces)
'''
pat = r"[a-z][a-z][a-z][a-z]"
Above pattern can also be written using quantifier
'''
pat = r"[a-z]{4}"
match_obj = re.search(pat, message)
print(match_obj)
'''
Output: <re.Match object; span=(4, 8), match='curr'>
'''

pat = r"[A-Z][a-z]{5}"
match_obj = re.search(pat, message)
print(match_obj)
'''
Output: <re.Match object; span=(12, 18), match='Python'>
'''

pat = r"[A-Z][a-z]{2,5}"
match_obj = re.search(pat, message)
print(match_obj)
'''
Output: <re.Match object; span=(0, 3), match='The'>
'''

pat = r"[A-Z][a-z]{4,}"
match_obj = re.search(pat, message)
print(match_obj)
'''
Output: <re.Match object; span=(12, 18), match='Python'>
'''

# Advanced Modifiers
pat = r"[A-Z][a-z]*?"
match_obj = re.search(pat, message)
print(match_obj)
'''
Output: <re.Match object; span=(0, 1), match='T'>
'''

pat = r"[A-Z][a-z]*+"
match_obj = re.search(pat, message)
print(match_obj)
'''
Output: <re.Match object; span=(0, 3), match='The'>
'''

