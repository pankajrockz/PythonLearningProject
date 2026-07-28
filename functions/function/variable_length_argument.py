# Variable Length Positional Argument - *args - Variable length positional arguments(0 to n).

def printShow(*args):
    print(args, type(args)) # It will use it in tuple.

printShow(10,2,3,19,23,28)

def add(*nums):
    return sum(nums)

result = add(10,2,3,19,23,28)
print(result)


def student_details(sid, sname, *marks):
    percent = sum(marks) / len(marks)
    print (f'{sname} with id {sid} secured {percent}')

student_details(102, 'Marks', 87.0, 69.6, 43.4, 45.3, 90.0)

# Variable length Keyword Argument - **kwargs - This argument should always be the last argument.

def func(**kwargs):
    print(kwargs, type(kwargs))

func(x=10, y=20)
func()

def student_detail(sid, sname, *extra, **marks):
    if(len(marks) == 0):
        print(f'{sname} did not attend the exam')
    else:
        percent = sum(marks.values()) / len(marks)
        print (f'{sname} with id {sid} secured {percent}')
    print(f'{sname} does {extra}')

student_detail(102, 'Marks', 'Football', sub1 = 87.0, sub2 = 69.6, sub3 = 43.4, sub4 = 45.3, sub5=90.0)
student_detail(103, "Carl", 'Tennis', 'Debates')