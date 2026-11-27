
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's Job.....")

class Developer(Employee):

    def doJob(self):
        print("Development Job.......")

def BankJob(emp):
    print('Bank job started......')
    emp.doJob()
    print("Bank job completed......")
    print("-" * 60)

mark = Manager()
tom = Developer()

BankJob(mark)
BankJob(tom)
