# Q3

# define the function
def Pascal_triangle(k):
    lis = [1] * k
    l = k - 1
    for i in range(k):
        m = 1
        n = 1
        for j in range(1,i+1):
            m = m * (k - j)
            n = n * j
        lis[i] = m / n
    print(lis)
                                
Pascal_triangle(200)