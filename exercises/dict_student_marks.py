student_details = {'Alice':85, 'Mark':65, 'Johny':76, 'Kailong':98, 'Yiming':54}

student_name = input("Enter the student's name: ")
marks = student_details.get(student_name)
if marks is not None:
    print(f"{student_name}'s marks: {marks}")
else:
    print("Student not found.")