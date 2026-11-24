# A function can remember variables from the environment in which it was created even after the outer function has
# finished executing


def outerFun():
    message = "Welcome to Adv Python"
    
    def innerFun():
        print("Hello World.....")
        print(message)

    return innerFun


inref = outerFun()
inref()