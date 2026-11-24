

def Banktask(fnc):
    print("Logging into the server......")
    fnc()           # callback
    print("Logging out of the server......")
    print("-" * 60)


def deposit():
    print("Amount successfully credited into the account.....")

def withdraw():
    print("Amount successfully debited from the account......")

Banktask(deposit)
Banktask(withdraw)