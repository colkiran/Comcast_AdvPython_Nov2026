
numbers = list(range(1, 6))
print(f"numbers :{numbers}")

# numbers is a list that is iterable
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

print("-" * 60)
x = 10
lst = [1, 2, 3, 4, 5]
print(f"x :{x}")
# print(iter(x))

print(dir(iter(lst)))
# __iter__ and __next__ are the protocols of iterable objects

print("-" * 60)
names = ['Sachin', 'Sourav', 'Rohit', 'Virat', 'Kapil', 'Gavaskar']
print(f"names: {names}")
for name  in names:
    print(name)

print("-" * 60)
iterObj = iter(names)
while True:
    try:
        elem = next(iterObj)
        print(f"elem :{elem}")
    except StopIteration:
        break