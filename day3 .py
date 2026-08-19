name="nancy"
def student():
  print(name)
  student()
print(name)

name="monisha"
age=20
def student():
    print(name)
    print(age)
student()

def student():
    age=27
    print(age)
student()

name="monisha"
age=20
def student():
    print(name)
    print(age)
student()

name="ramu"
name="ammu"
def display():
    name="ravi"
    name="anu"
    print(name)
display()
print(name)

def square(x):
    return x*x
print(square(5))


square=lambda x:x*x
print(square(5))

cube=lambda x:x*x*x
print(cube(5))

add=lambda x:x+x
print(add(5))

large=lambda x,y:x if x>y else y
print(large(10,20))

def countdown(n):
    if n==0:
       return
    print(n)
    countdown(n-1)
countdown(5)

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(6) 

def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print(power(2,4))
