class student:
    def display(self):
        print("AIDS students are good")
s1=student()
s1.display()

class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1=student("Alice", 20)
s1.display()

class employee:
    def __init__(self,name,age,salary,department):
        self.name=name
        self.age=age
        self.salary=salary
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)
        print("Department:",self.department)
e1=employee("John", 30, 50000, "IT")
e2=employee("Alice", 25, 60000, "HR")
e1.display()
print()
e2.display()

class student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll No:",self.rollno)
s1=student("Bob", 20, 123)
s1.display()


class Employee(ABC):
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Department:", self.department)