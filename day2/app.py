age = 20
print(type(age))

cgpa=8.7544444
print(type(cgpa))

name="ammu"
print(type(name))

usn=43768
cgpa=8.655
result="pass"
print(type(usn))
print(type(cgpa))
print(type(result))

marks=80
if marks>=65:
    print("pass")
else:
    print("fail")

name=input("Enter the name")
college=input("Enter the college name")
cgpa=input("Enter the college name")
print("welcome to RIT",name)
print("yor are studying at",college)
print("your CGPA IS",cgpa)

a=int(input())
b=int(input())
print(a+b)  

a=float(input("enter a first number:"))
b=float(input("enter a second number:"))
print(a+b) 
print(a-b)
print(a*b)
print(a/b)
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

a=int(input("Enter a number"))
if a>0:
    print("Positive number")
elif a<0:
    print("Negative number")
else:
    print("The number is zero")

crt_pin="2123"
pin=input("Enter a number")
if pin==crt_pin:
    print("login successful")
else:
    print("error! try again")


for i in range(0,10):
    print("Welcome")


for i in range(3):
    for j in range(5):
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
