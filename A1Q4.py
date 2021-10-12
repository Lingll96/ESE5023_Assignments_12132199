# Q4

import random

# define the function
def Least_moves(x):
    path = 0
    while x > 1:
        if x%2 == 0:
            x = x/2
            path += 1
        else:
            x = x - 1
            path += 1
    print(path)
        
# check
x = random.randint(1,101)
print(x)
Least_moves(x)