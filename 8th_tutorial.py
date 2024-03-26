dictionary = {'a':1, 'b':2, 'c':'d'}

dictionary['c']
dictionary.keys()
dictionary.values()


dictionary.items()

dictionary[3] = 'e'
dictionary

dictionary['c'] = 'e'
dictionary








print(y)

'a'+1

import math
math.sqrt(-1)


a = 0.1
if type(a)!=int:
    raise TypeError("not integer!")
    
    
    
    
    
    
    
    

while True:
a = input('give the input : ')

if a == 'endinput':
    break
try :
    a = int(a)
    print('')
    print(a,'well written')
except ValueError:
    pass
    
    
    
    
    
    
    
    
c = 1+2j
c.real
c.imag
abs(c)
abs(c) == math.sqrt(c.real**2+c.imag**2)


a = 3
a * 1j

cmath.exp(1+1j)

cmath.exp(1+1j)
cmath.phase(1+1j)
cmath.phase(1+1j) == cmath.pi/4



















#HW2

import math


def produce_bell(n):
    if n == 0:
        return 1
    
    if n == 1:
        return 1
    for i in range(1, n + 1):
        bell_number = 0
        for k in range(i):
            bell_number += math.comb(i - 1, k) * produce_bell(k)
    return bell_number

# Test the function
n = 100
bell_numbers = produce_bell(n)
print(bell_numbers)



#HW2
import math


def produce_bell(n):
    bell_numbers = {0:1}
    for i in range(1, n + 1):
        bell_number = 0
        for k in range(i):
            bell_number += math.comb(i - 1, k) * bell_numbers[k]
        bell_numbers[i] = bell_number
    return bell_numbers[n]

# Test the function
n = 10
bell_numbers = produce_bell(n)
print(bell_numbers)