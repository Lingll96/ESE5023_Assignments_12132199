# Q1

# input 3 numbers
a = int(input('please input the first number: '))
b = int(input('please input the second number: '))
c = int(input('please input the third number: '))

# comparation
if a > b:
    if b > c:
        print(str(a)+', '+str(b)+', '+str(c))
    elif a > c:
        print(str(a)+', '+str(c)+', '+str(b))
    else:
        print(str(c)+', '+str(a)+', '+str(b))
else:
    if b > c:
        pass
    else:
        print(str(c)+', '+str(b)+', '+str(a))