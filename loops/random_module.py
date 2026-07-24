import random

# random() - return random float between 0.0 to 1.0(excluded)
print(random.random())

# randInt(a,b) - return random integer between a and b(both included
print(random.randint(10, 15))

nums = [10, 4, 1, 8, 4, 3]

# choice(sequence) - return a random item from the sequence
print(random.choice(nums))

# suffle(sequence) - returns the element shuffled in random order
random.shuffle(nums)
print(nums)