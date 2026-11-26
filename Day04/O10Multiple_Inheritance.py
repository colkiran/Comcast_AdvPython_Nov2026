
class Animal:

    def __init__(self):
        self.a = 10
        print("Animal Ctor......")

    def eat(self):
        print("Animal eats.....")

    def fun(self):
        print("Fun method of Animal class")

class Person:

    def __init__(self):
        self.p = 20
        print("Person Ctor.......")

    def talk(self):
        print("Person talks.....")

    def fun(self):
        print("Fun method of Person class")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()
        Person.__init__(self)
        self.g = 30
        print("Girl Ctor.....")

gracie = Girl()
gracie.eat()
gracie.talk()
gracie.fun()        # which fun method is called (Animal or Person)


print('-' * 60)
print(gracie.__dict__)
