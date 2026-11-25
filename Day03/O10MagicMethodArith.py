
class Employee:

    def __init__(self, name, salary):
        self.name= name
        self.salary = salary


    def __str__(self):
        return "Name is {} and Salary is {}".format(self.name, self.salary)

    def __add__(self, other):
        return Employee("noName", self.salary + other.salary)

    def __sub__(self, other):
        return Employee("", self.salary - other.salary)

    def __mul__(self, other):
        return Employee("", self.salary * other.salary)

    def __truediv__(self, other):
        return Employee("", self.salary / other.salary)

    def __floordiv__(self, other):
        return Employee("", self.salary // other.salary)
    

emp1 = Employee("Jack", 15000)
print(emp1)
print("-" * 60)

emp2 = Employee("Jill", 20000)
print(emp2)
print("-" * 60)

emp3 = Employee("Humpty", 30000)
print(emp3)
print("-" * 60)

print("Addition".center(60, "-"))
print(emp1 + emp2 + emp3)

print("Subtraction".center(60, "-"))
print(emp2 - emp1 - emp3)

print("Multiplication".center(60, "-"))
print(emp1 * emp2)

print("Division".center(60,"-"))
print(emp1 / emp2)

print("Floordiv".center(60, "-"))
print(emp2 // emp1)