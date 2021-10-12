# Q5.1

def Find_expression(x):
    import numpy
    import random
    
    # creat a matrix including all of the numbers
    M = numpy.random.randint(0,1,81).reshape((9,9))
    for i in range(9):
        for j in range(i+1):
            m = int(M[i,j])
            for k in range(i-j+1):
                m = m + (i + 1 - k) * (10 ** k)
            M[i,j] = m
    

    # get all of the possibilities of the combination of numbers
    def copy(a):
        a_copy = a.copy()
    def appe(i,x,a):
        if M[i,x] != 0:
            a.append(M[i,x])
    def dele(a):
        if len(a) >= 2:
            del a[-1]
            del a[-1]
        elif len(a) == 1:
            del a[-1]
        else:
            pass
        return
    def det1(i,x,a,b):
        if i == 8:
            b.append(a[:])
            del(a)
            return
        else:
            return
            
    
    # aal is all of the possibilities, al is one of the possibility
    aal = []
    al = []
    for a in range(0,9):
        appe(a,0,al)
        det1(a,0,al,aal)
        if a == 8:
            dele(al)
            break
            
        else:
            for b in range(a+1,9):
                appe(b,a+1,al)
                det1(b,a+1,al,aal)
                if b == 8:
                    dele(al)
                    break

                else:
                    for c in range(b+1,9):
                        appe(c,b+1,al)
                        det1(c,b+1,al,aal)
                        if c == 8:
                            dele(al)
                            break

                        else:
                            for d in range(c+1,9):
                                appe(d,c+1,al)
                                det1(d,c+1,al,aal)
                                if d == 8:
                                    dele(al)
                                    break

                                else:
                                    for e in range(d+1,9):
                                        appe(e,d+1,al)
                                        det1(e,d+1,al,aal)
                                        if e == 8:
                                            dele(al)
                                            break

                                        else:
                                            for f in range(e+1,9):
                                                appe(f,e+1,al)
                                                det1(f,e+1,al,aal)
                                                if f == 8:
                                                    dele(al)
                                                    break

                                                else:
                                                    for g in range(f+1,9):
                                                        appe(g,f+1,al)
                                                        det1(g,f+1,al,aal)
                                                        if g == 8:
                                                            dele(al)
                                                            break

                                                        else:
                                                            for h in range(g+1,9):
                                                                appe(h,g+1,al)
                                                                det1(h,g+1,al,aal)
                                                                if h == 8:
                                                                    dele(al)
                                                                    break

                                                                else:
                                                                    appe(8,8,al)
                                                                    det1(8,8,al,aal)
                                                                    dele(al)
    
    # add and minus
    def add(a,b):
        return (a + b)
    def minus(a,b):
        return(a - b)
    def choose1(i,a,b):
        if i == 0:
            return add(a,b)
        else:
            return minus(a,b)
    def choose2(i,a):
        if i == 0:
            return ''.join([a,' + '])
        else:
            return ''.join([a,' - '])
    
    
    # judge, in 5.1, 'print(b)' is needed
    def end_det(x,a,b):
        if a == x:
            #print(b)
            return 1;
        else:
            return 0
            
    # variables
    l_aal = len(aal)
    count = 0
    
    # choose add or minus
    for i in range(l_aal):
        l_i = len(aal[i])
        a = 0
        j = 0
        sum = aal[i][0]
        expr = str(aal[i][0])
        if j == l_i - 1:
            expr = ''.join([expr,' = ' + str(sum)])
            count = count + end_det(x,sum,expr)
            continue
        while a < 2:
            sum_copya = sum
            expr_copya = expr
            sum = choose1(a,sum,aal[i][j + 1])
            expr = choose2(a,expr)
            j += 1
            a += 1
            b = 0
            expr = expr + str(aal[i][j])
            if j == l_i - 1:
                expr = ''.join([expr,' = ' + str(sum)])
                count = count + end_det(x,sum,expr)
                sum = sum_copya
                expr = expr_copya
                j -= 1
                continue
            else:
                while b < 2:
                    sum_copyb = sum
                    expr_copyb = expr
                    sum = choose1(b,sum,aal[i][j + 1])
                    expr = choose2(b,expr)
                    j += 1
                    b += 1
                    c = 0
                    expr = expr + str(aal[i][j])
                    if j == l_i - 1:
                        expr = ''.join([expr,' = ' + str(sum)])
                        count = count + end_det(x,sum,expr)
                        sum = sum_copyb
                        expr = expr_copyb
                        j -= 1
                        continue
                    else:
                        while c < 2:
                            sum_copyc = sum
                            expr_copyc = expr
                            sum = choose1(c,sum,aal[i][j + 1])
                            expr = choose2(c,expr)
                            j += 1
                            c += 1
                            d = 0
                            expr = expr + str(aal[i][j])
                            if j == l_i - 1:
                                expr = ''.join([expr,' = ' + str(sum)])
                                count = count + end_det(x,sum,expr)
                                sum = sum_copyc
                                expr = expr_copyc
                                j -= 1
                                continue
                            else:
                                while d < 2:
                                    sum_copyd = sum
                                    expr_copyd = expr
                                    sum = choose1(d,sum,aal[i][j + 1])
                                    expr = choose2(d,expr)
                                    j += 1
                                    d += 1
                                    e = 0
                                    expr = expr + str(aal[i][j])
                                    if j == l_i - 1:
                                        expr = ''.join([expr,' = ' + str(sum)])
                                        count = count + end_det(x,sum,expr)
                                        sum = sum_copyd
                                        expr = expr_copyd
                                        j -= 1
                                        continue
                                    else:
                                        while e < 2:
                                            sum_copye = sum
                                            expr_copye = expr
                                            sum = choose1(e,sum,aal[i][j + 1])
                                            expr = choose2(e,expr)
                                            j += 1
                                            e += 1
                                            f = 0
                                            expr = expr + str(aal[i][j])
                                            if j == l_i - 1:
                                                expr = ''.join([expr,' = ' + str(sum)])
                                                count = count + end_det(x,sum,expr)
                                                sum = sum_copye
                                                expr = expr_copye
                                                j -= 1
                                                continue
                                            else:
                                                while f < 2:
                                                    sum_copyf = sum
                                                    expr_copyf = expr
                                                    sum = choose1(f,sum,aal[i][j + 1])
                                                    expr = choose2(f,expr)
                                                    j += 1
                                                    f += 1
                                                    g = 0
                                                    expr = expr + str(aal[i][j])
                                                    if j == l_i - 1:
                                                        expr = ''.join([expr,' = ' + str(sum)])
                                                        count = count + end_det(x,sum,expr)
                                                        sum = sum_copyf
                                                        expr = expr_copyf
                                                        j -= 1
                                                        continue
                                                    else:
                                                        while g < 2:
                                                            sum_copyg = sum
                                                            expr_copyg = expr
                                                            sum = choose1(g,sum,aal[i][j + 1])
                                                            expr = choose2(g,expr)
                                                            j += 1
                                                            g += 1
                                                            h = 0
                                                            expr = expr + str(aal[i][j])
                                                            if j == l_i - 1:
                                                                expr = ''.join([expr,' = ' + str(sum)])
                                                                count = count + end_det(x,sum,expr)
                                                                sum = sum_copyg
                                                                expr = expr_copyg
                                                                j -= 1
                                                                continue
                                                            else:
                                                                while h < 2:
                                                                    sum_copyh = sum
                                                                    expr_copyh = expr
                                                                    sum = choose1(h,sum,aal[i][j + 1])
                                                                    expr = choose2(h,expr)
                                                                    h += 1
                                                                    expr = ''.join([expr,str(aal[i][j + 1]) + ' = ' + str(sum)])
                                                                    count = count + end_det(x,sum,expr)
                                                                    sum = sum_copyh
                                                                    expr = expr_copyh
                                                            
                                                            sum = sum_copyg
                                                            expr = expr_copyg
                                                            j -= 1
                                                    sum = sum_copyf
                                                    expr = expr_copyf
                                                    j -= 1
                                            sum = sum_copye
                                            expr = expr_copye
                                            j -= 1
                                    sum = sum_copyd
                                    expr = expr_copyd
                                    j -= 1
                            sum = sum_copyc
                            expr = expr_copyc
                            j -= 1
                    sum = sum_copyb
                    expr = expr_copyb
                    j -= 1
            sum = sum_copya
            expr = expr_copya
            j -= 1
    return count

# Q5.2

# get the list
def Total_solutions(x):
    a = []
    for i in range(1,x + 1):
        a.append(Find_expression(i))
    return a

# define variables
Total_solutions = Total_solutions(100)
M = max(Total_solutions)
m = min(Total_solutions)
M_count = Total_solutions.count(M)
m_count = Total_solutions.count(m)
M_list = []
m_list = []

# fine the numbers yield the max and min
Total_solutions_copy = Total_solutions[:]
for i in range(M_count):
    M_list.append(Total_solutions.index(M) + i + 1)
    Total_solutions.remove(M)
Total_solutions = Total_solutions_copy[:]
for i in range(m_count):
    m_list.append(Total_solutions.index(m) + i + 1)
    Total_solutions.remove(m)
Total_solutions = Total_solutions_copy[:]
    
print(Total_solutions)
print('最大值为'+str(M)+'，取得最大值的数为'+str(M_list)+'。')
print('最小值为'+str(m)+'，取得最小值的数为'+str(m_list)+'。')
    