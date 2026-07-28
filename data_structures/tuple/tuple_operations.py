#Concatenation - +
student_details1 = (1001, "John")
student_details2 = (78.5, 91.0, 83.5, 79.5)

student_details = student_details1 + student_details2
print(student_details)

#Repetition Operation - *
t1 = "Class 5", 5000
print(t1*3)

#Membership Operation - In / not In
print(91 in student_details2)
print(99 not in student_details2)

#Count Operation
t2 = 10, 41, 9, 0, 3, 0
print(t2.count(41))

#Index Operation
print(t2.index(0))

#Min Operation
print(min(t2))

#Max Operation
print(max(t2))

#Sum Operation
print(sum(t2))