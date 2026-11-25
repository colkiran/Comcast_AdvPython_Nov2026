
class Player:           # pascal casing

    def get_runs(self):
        print("runs scored......")

sachin = Player()
print(type(sachin))
print(sachin.__class__)
sachin.get_runs()

print("-" * 60)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
