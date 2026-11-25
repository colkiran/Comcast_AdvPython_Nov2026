

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
       return f"Name :{self.name}\nSalary :{self.salary}"

    # it works for not equal to also
    def __eq__(self, other):
        return self.salary == other.salary

    # it works for less than also
    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee("Tom", 45000)
print(emp1)

print("-" * 60)
emp2 = Employee("Alice", 65000)
print(emp2)

print("-" * 60)
# need is to compare the salaries
# comparing the address
print(emp1 != emp2)

print("-" * 60)
print(emp1 < emp2)
