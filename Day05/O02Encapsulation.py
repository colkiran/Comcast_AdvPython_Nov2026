
class BankAccount:

    def __init__(self, owner: str, initial_bal: float):
        self.owner = owner
        self.__balance = initial_bal            # private var

    # controlled public interface to modify private data
    def deposit(self, amount: float):
        if  amount <= 0:
            raise ValueError("Deposit amount must be positive...")
        else:
            self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError("Insufficient funds...")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Alex", 250.00)
account.deposit(500)
print(account.get_balance())

