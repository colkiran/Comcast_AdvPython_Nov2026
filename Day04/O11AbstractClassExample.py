
# an abstract class is a blueprint for other class, it defines what should be the behaviour of the child class

from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Account....")

    @abstractmethod
    def getBalance(self):
        pass

    def withDraw(self):
        pass

class Savings(Account):
    def deposit(self):
        print("Amount credited into the account successfully...")

    def getBalance(self):
        print("Balance in account ending xxxx is ######.##")

sav = Savings()
sav.getBalance()
sav.deposit()


