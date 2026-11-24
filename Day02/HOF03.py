

def Banktask(fnc):
    def helperFun(args):
        print("Logging into the server......")
        fnc(args)           # callback
        print("Logging out of the server......")
        print("-" * 60)
    return helperFun

def deposit(amt):
    print(f"Amount of {amt} successfully credited into the account.....")

def withdraw(amt):
    print(f"Amount of {amt} successfully debited from the account......")

# depref = Banktask(deposit)
# witref = Banktask(withdraw)
#
# depref(50000)
# witref(15000)


deposit = Banktask(deposit)
withdraw = Banktask(withdraw)

deposit(35000)
withdraw(10000)
