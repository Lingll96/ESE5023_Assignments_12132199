# Q2.1

import numpy
import random

# creat random matrixes
M1 = numpy.random.randint(0,51,50).reshape((5,10))
M2 = numpy.random.randint(0,51,50).reshape((10,5))

# Q2.2

# creat a zero matrixes
M = numpy.random.randint(0,1,25).reshape((5,5))

# multiply
for i in range(5):
    for k in range(5):
        for j in range(10):
            n = int(M[i,k])
            n = n + (int(M1[i,j]) * int(M2[j,k]))
            M[i,k] = numpy.int(n)

# check
print(str(M1)+'\n'+str(M2)+'\n'+str(M))