s1 = "We are learning Python. Python is very easy"

#Membership Operations - in / not in
print("Python" in s1)
print("Python" not in s1)

#Strip -
s2 = "    Pyhton    "
print(s2.strip())
print(s2.lstrip())
print(s2.rstrip())

#Replace -
print(s1.replace("Python", "Java"))
print(s1.replace("Python", "Java",1))

# Changing cases of a string
#upper(), lower(), title(), capatilize()
s3 = "Python3.14"
print(s3.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())
print(s1)

#Starts with and ends with

print(s1.startswith("We are"))
print(s1.endswith("We are"))
print(s1.startswith("very easy"))
print(s1.endswith("very easy"))