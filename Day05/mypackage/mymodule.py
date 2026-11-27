
myCountry= "India"

countries = ['America', 'Brazil', 'Canada', 'Denmark', 'Egypt', 'France', 'Germany']

capitals = ({'America': 'Washington', 'Brazil': 'Brasalia', 'Canada': 'Ottawa', 'Denmark': 'Copenhagen', 'Egypt': 'Cairo', 'France': 'Paris', 'Germany': 'Berlin'})

def Greet(gstname):
    print(f"Greeting Mr.{gstname}, Welcome to the event.....")

class Employee:

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def get_details(self):
        print(f"Name of the employee is {self.name} who is {self.age} years old and working for {self.dept} dept")

# print(f"Module_Name :{__name__}")

if __name__ == '__main__':
    print(myCountry)

    print("-" * 60)

    print(capitals)

    print("-" * 60)

    emp1 = Employee("Bob", 48, "Network Security")

    emp1.get_details()


