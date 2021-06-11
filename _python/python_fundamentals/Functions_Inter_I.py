# With this concept of default parameters in mind, the goal of this assignment is to write a single function, randInt() that takes up to 2 arguments.
# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.

import random
def randInt(min=0, max=100):
    num = random.random() * max
    if num < min:
        return int(min)
    else:
        return int(num)

print(randInt(0,500))
print(randInt())


