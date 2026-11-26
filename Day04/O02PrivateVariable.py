
class Employee:

    def __init__(self, name, age):
        self.__name = name      # private variable
        self.age = age
        self.tech = ['Python', 'Machine Learning', "Artificial Intelligence", "Deep Learning", "Data Science", "Data Analytics"]

    def __str__(self):
        return self.__name + " - " + ", ".join([str(v) for v in self.tech])

emp1 = Employee("Steve", 32)
print(emp1)

print("-" * 60)
# print(emp1.__name)
print(emp1.__dict__)

print("-" * 60)
emp1._Employee__name = "Ricards"
print(emp1)
