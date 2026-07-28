#Nested loops - Loops under a loop.
for i in range(3):
    for j in range(2):
        print(f'i = {i}, j = {j}')

for i in range(6):
    for j in range(i):
        print("*", end=' ')
    print()