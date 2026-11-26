
class Product:

    def __init__(self, price):
        self.__price = price

    def get_price(self):
        print("getter called.....")
        return self.__price

    def set_price(self, val):
        print("setter called.....")
        self.__price = val

    def del_price(self):
        print("deleter called....")
        self.__price = 0

    price = property(get_price, set_price, del_price)

prd1 = Product(100)
print(prd1.price)       # calls the getter method
prd1.price = 85
print(prd1.price)
del prd1.price
print(prd1.price)

