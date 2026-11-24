
# lambdas are single line expression

def addMe(x, y):
    return x + y

# print(addMe(10, 20))
a = addMe
res = a(15, 20)
print(res)

print("-" * 60)

b = lambda x, y: x + y
res = b(30, 40)
print(res)

# lambdas are best used with 'map', 'reduce' and filters

print("map".center(60, "-"))
# map - will have an expression and will iterate through a collection and implement the expression on every element

l = list(range(1, 11))
print(f"l :{l}")

squares =  list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")


