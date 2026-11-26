
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        if (val < 0):
            raise ValueError("Price cannot be less than zero.....")
        else:
            self.__price = val

    def del_price(self):
        self.__price = 0

import sys
try:
    prd1 = Product(30)
    print(prd1.get_price())
    prd1.set_price(65)
    print(prd1.get_price())
    prd1.del_price()
    print(prd1.get_price())

except:
    print("Exception Occurred...")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
