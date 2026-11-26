
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.age = 1

    def eat(self):
        print("Animals eat....")

class  Bird(Animal):
    # overriding parent class constructor
    def __init__(self):
        super().__init__()
        self.weight = '3 kg'
        print("Bird Ctor......")

    def fly(self):
        print("Birds fly.....")

dolphin = Bird()
dolphin.fly()
dolphin.eat()

print("-" *  60)
print(dolphin.__dict__)



