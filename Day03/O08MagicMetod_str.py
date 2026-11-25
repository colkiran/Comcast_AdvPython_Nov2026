
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
       return f"Name :{self.name}\nAge :{self.age}"

ply1 = Player("Sachin", 38)
# ply1.get_details()

print("-" * 60)
print(str(ply1))

print("-" * 60)
print(ply1)