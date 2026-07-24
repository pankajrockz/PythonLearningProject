'''
>=90, grade A
80 and 89, grade B
70 and 79, grade C
60 and 69, grade D
<60, grade F
'''

marks = float(input('Enter marks: '))
if 90 <= marks <= 100: #we can also use marks<=90 and marks <=100
    print(f'{marks} - Grade A')
elif 80 <= marks < 90:
    print(f'{marks} - Grade B')
elif 70 <= marks < 80:
    print(f'{marks} - Grade C')
elif 60 <= marks < 70:
    print(f'{marks} - Grade D')
else:
    print(f'{marks} - Grade F')