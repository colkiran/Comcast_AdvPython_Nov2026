from datetime import  date
class Employee:

    def __init__(self, name, dob):
        self.name = name
        self.dob = date(int(dob.split("-")[2]), int(dob.split("-")[1]), int(dob.split("-")[0]))

    def __str__(self):
        return f"Name :{self.name}\nAge :{Employee.age(self.dob)}"

    @staticmethod
    def age(db):
        return (date.today().year - db.year)

emp1 = Employee("John", "15-06-1982")
print(emp1)
