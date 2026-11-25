
class Player:

    # class attribute (class variable), values will the same across objects
    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self will have the name of the object that made a call to the method

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")
        print("-" * 60)


    @classmethod
    def change_team(cls, new_team):
        cls.team = new_team

ply1 = Player("rohit", 32)
ply2 = Player("virat", 33)

Player.change_team("Sahara")

print(f"Team :{ply1.team}")
ply1.get_details()

print(f"Team :{ply2.team}")
ply2.get_details()




