
class Employee:

    def __init__(self, name, salary):
        self.name= name
        self.salary = salary
        self.tech = ['C++', 'Python', "AWS", 'Hadoop', 'Spark', 'Airflow', 'Scala']


    def __str__(self):
        return "Name is {} and Salary is {}".format(self.name, self.salary)

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

emp1 = Employee("Kevin", 30000)
print(emp1)
print("-" * 60)

emp2 = Employee("Richard", 10000)
print(emp2)
print("-" * 60)

print(len(emp1))
print("-" * 60)

print([tech for tech in emp1])
