

def Banktask(fnc):
    def helperFun(args):
        print("Logging into the server......")
        fnc(args)           # callback
        print("Logging out of the server......")
        print("-" * 60)
    return helperFun

@Banktask
def deposit(amt):
    print(f"Amount of {amt} successfully credited into the account.....")


# call the Banktask function and return the reference of helper function with the name withdraw
@Banktask
def withdraw(amt):
    print(f"Amount of {amt} successfully debited from the account......")

deposit(35000)
withdraw(10000)
