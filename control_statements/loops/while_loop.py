#While - While loop is a condition based loop and runs the code block until the condition is satisfied.
# while condition:
#     statements

num =1
while num < 5:
    print(num)
    num += 1

#Infinite While loop
# num =1
# while num < 5:
#     print(num)

#Password program until the correct password matches
correct_password = "Python"

while True:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Password match!!!!")
        break
    else:
        print("Password not match!!!")
print("Thank you for your time!")