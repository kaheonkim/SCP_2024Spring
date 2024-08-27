a = int(input("enter the numbers(integer):"))
b = int(input("enter the numbers(integer):"))
c = int(input("enter the numbers(integer):"))

D = b**2 - 4*a*c

if D > 0:
    print("Two real solutions")
    
if D < 0:
    print("Two imaginery solutions")

else:
    print("One real solution")