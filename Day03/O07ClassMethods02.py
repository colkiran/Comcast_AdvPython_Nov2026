
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
    def CreatePlayer(cls, fname, lname, age):
        print("factory.....")
        return cls(f"{fname} {lname}", age)


ply1 = Player("rohit", 30)
ply1.get_details()


ply2 = Player.CreatePlayer("Virat", "Kholi", 31)
ply2.get_details()
