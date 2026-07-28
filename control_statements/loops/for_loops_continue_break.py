#Continue - Continue transfer the control to the loop net iteration without running the below code blocks.
for num in range(10):
    if num % 3 == 0:
        continue
    print(num)

#Break - Break statement terminates the loop
for num in range(1, 10):
    if num % 3 == 0:
        break
    print(num)