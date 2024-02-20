#1st exercise
tolerance = float(input("Please enter a positive error tolerance: "))
s = 0
term = 0
k = 0
while k >=0 :
    a = ((-1)**(k))*(k+3)/(k**3+k+1)
    k += 1
    s += a
    term = term + 1
    if abs((k+4)/((k+1)**3+k+2)) < tolerance:
        break
print(s)
print(term)



#2nd exercise

def compounding(r, D, N):
    s = D
    for i in range(1, N+1):
        s += D*(1+r/100)**i
    return s

def geometric(r,D,N):
    s = D*((1+r/100)**(N+1)-1)/(1+r/100-1)
    return s


#3rd exercise

import math

def Heron(a,b,c):
    s = (a+b+c)/2
    A2 = s*(s-a)*(s-b)*(s-c)
    A = math.sqrt(A2)
    return A


#4th exercise

def tribonacci(n):
    a0, a1, a2 = 0, 0, 1
    if n ==0:
        return a0
    elif n ==1:
        return a1
    elif n ==2:
        return a2
    else:
        for i in range(3,n+1):
            a3 = a0 + a1 + a2
            a0, a1, a2 = a1, a2, a3
        return a2

def tribonacci_modified(n, a0 = 0, a1=1, a2=1):
    if n ==0:
        return a0
    elif n ==1:
        return a1
    elif n ==2:
        return a2
    else:
        for i in range(3,n+1):
            a3 = a0 + a1 + a2
            a0, a1, a2  = a1, a2, a3
