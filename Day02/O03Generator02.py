
def fun():
    n = 1
    print("Apples from ooty....")
    yield n
    n += 9
    print("Oranges from Kanpur")
    yield n
    n += 10
    print("Grapes from Hubli")
    yield n

res = fun()
print(f"res: {res}")
print(res.__next__())
print(res.__next__())
print(res.__next__())
# print(res.__next__())

print("-" * 60)
for x in fun():
    print(x, end=" ")
print()
