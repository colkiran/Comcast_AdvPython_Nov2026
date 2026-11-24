
def callMe():
    print("Apples from ooty.....")


def fun(fnc):
    print("Hello......")
    fnc()
    print("Hi.......")
    print("-" * 60)

    def defineMe():
        print("Oranges from kanpur......")

    return defineMe

def funcallback(fnc):
    print("Mera bharat mahan.....")
    fnc()
    print("India is great.......")

funcallback(fun(callMe))
