
class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tech = ['C++', 'Python', 'AWS', 'Devops', 'Spark', 'Airflow', 'Kafka', 'Hadoop']

    def __str__(self):
        return f"Name :{self.name}\nAge :{self.age}"

    def __iter__(self):
        return iter(self.tech)

    def append(self, value):
        self.tech.append(value)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, val ):
        self.tech[index] = val

emp1 = Employee("Kevin", 29)
emp1.name = "Micheal"
print(emp1)

print("-" * 60)
print([t for t in emp1])

print("-" * 60)
emp1.append("Debizium")

print("-" * 60)
print([t for t in emp1])

print("-" * 60)
res = emp1[2]
print(f"res :{res}")

print("-" * 60)
emp1[3] = "Docker"

print("-" * 60)
print([t for t in emp1])
