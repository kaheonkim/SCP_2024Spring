for i in range(1,11):
    for value in range(1,i+1):
        print(f"{value:>3}", end=" ")
    print()
    
    
    
    
    
    
def prod(a1,a2,a3,a4,x,y):
    x_output = a1*x + a2*y
    y_output = a3*x + a4*y
    return x_output, y_output




def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))



import math
def T(n):
    if n == 1:
        return 2
    else:
        return 3+T(math.ceil(n/2))

def benchmark(n):
    return 3*math.log2(n)+2


def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage
print(sum_of_digits(12345))  # Output: 15 (1 + 2 + 3 + 4 + 5)
print(sum_of_digits(987654321))




