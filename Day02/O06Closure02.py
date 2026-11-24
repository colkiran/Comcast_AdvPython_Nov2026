
def outerFun(greet):

    def innerFun(gname):
        print(greet, gname)

    return innerFun

outerFun("Welcome")("Sachin")

print("-" * 60)
# curry
engGrt = outerFun("Welcome")
tmlGrt = outerFun("Vanakam")

# simple curry
engGrt("Rahul")
tmlGrt("Ashwin")
