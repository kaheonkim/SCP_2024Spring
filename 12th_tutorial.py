import math

def func(x=1,y=2,z=10):
    return (x+y+z)
print(func())
print(func(x=2,y=3))
print(func(y=3,x=2))



def func2(*args):
    sum_ = 0
    for i in args:
        sum_+=i
    return sum_
print(func2(1,2,3))
print(func2(1,2,3,4,5))






def function_input(f, x,y):
    return f(x,y)

def f(x,y):
    return x+y
print(function_input(f, 1,2))
print(function_input(lambda x,y:x+y, 1,2))
print(function_input(lambda x,y:x*y, 10,20))



# # Not working
# def function_output(f,g):
#     return f+g
# h = function_output(lambda x,y:x+y, lambda x,y: x*y)


def function_output(f,g):
    def h(x,y):
        return f(x,y)+g(x,y)
    return h
h = function_output(lambda x,y:x+y, lambda x,y: x*y)
print(h(2,3))


class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
print(p1.name)
print(p1.age)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()




p1.age = 40
p1.__str__()






class arithmetic:
    def __init__(self, xx,yy):
        self.x = xx
        self.y = yy
    def add(self):
        return self.x + self.y
    def subt(self):
        return self.x - self.y
    def mult(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y
    def l_dist(self, order):
        return (abs(self.x)**order+abs(self.y)**order)**(1/order)
arith = arithmetic(3,4) 
print(arith.add())
print(arith.subt())
print(arith.mult())
print(arith.div())
print(arith.l_dist(2))
