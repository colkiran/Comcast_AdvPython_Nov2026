
class Player:

    def __init__(self):
        self.name = "Sachin"
        self.age = 35

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")

ply1 = Player()
ply1.get_details()

ply2 = Player()
ply2.name = "rohit"
ply2.age = 26
ply2.get_details()
