
# HOF
def fun():
    print("hello World")

    def innerFun():
        print("Hello from inner function.....")

    def innerfun2():
        print("Hai....")

    return innerFun, innerfun2



# fun()()     # calls the innerfun

print("-" * 60)
inrfunref = fun()
print(inrfunref)
for ref in inrfunref:
    ref()



