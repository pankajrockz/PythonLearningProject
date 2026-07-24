'''
if marks >= 60, student is pass else student is fail
and if the student is pass, then we print the grade
    >=90, grade A
    80 and 89, grade B
    70 and 79, grade C
    60 and 69, grade D
    <60, grade F
'''

marks = float(input('Enter marks: '))
if marks >= 60:
    print(f'Congrats! You are passed the exam with marks {marks}')
    if marks >= 90:
        print(f'{marks} - Grade A')
    elif 80 <= marks < 90:
        print(f'{marks} - Grade B')
    elif 70 <= marks < 80:
        print(f'{marks} - Grade C')
    else:
        print(f'{marks} - Grade D')
else:
    print(f'You have failed with marks {marks}, study hard next time!')
