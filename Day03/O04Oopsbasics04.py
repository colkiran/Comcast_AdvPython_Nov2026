
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self will have the name of the object that made a call to the method

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")

ply1 = Player("virat", 30)
ply1.get_details()

ply2 = Player("rohit", 29)
ply2.get_details()

print("-" * 60)
print(ply1.__dict__)
print(ply2.__dict__)
ply2.runs = 120
print(ply2.__dict__)
print(ply1.__dict__)
