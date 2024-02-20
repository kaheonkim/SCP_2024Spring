#1st exercise
for i in range(10):
    print(i)

    
#2nd exercise

s = 0

for i in range(1,21):
    s += i
print(s)
#210



#3rd exercise

s = 0
n = 15
for i in range(0,n+1):
    s += 2 * 3**i
print(s)
#43046720



#4th exercise

prod = 1

for i in range(1,8+1):
    prod *= i
print(prod)
#40320


#5th exercise

for i in range(5):
    for j in range(6):
        print("i: %d, j: %d"%(i,j))

#6th exercise

import math
s = 0
n, m = 5, 6
for i in range(0,n+1):
    for j in range(0,m+1):
        s += math.log(i**2+j**2+4*i*j+1)
print(s)
#144.70118842898816



#7th exercise

import math
s = 0 
for i in range(0, 101):
    #0~100
    fact = 1
    
    for j in range(1,i+1):#0~i
        fact *= j 
        
    s += 5**i/fact

print(s)
print(math.exp(5))

#148.41315910257657


#8th exercise


s = 0

for i in range(1,100+1):
    if (i % 2 == 0):
        s+= 1
        
print(s)



#9th exercise


s1 = 0
for x in range(1,10+1):
    for y in range(1,15+1):
        if (y>x>0):
            s1 += 8*x*y 
print(s1)

s2 = 0
for x in range(1,10+1):# x = 1 to 10
    for y in range(x+1, 15+1): # j = x+1, 15
        s2 += 8*x*y
        
print(s2)

#39160
