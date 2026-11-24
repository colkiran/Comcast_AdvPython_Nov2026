
from sys import getsizeof

v1 = [x ** 2 for x in range(1, 11)]                 # Comprehensions
print(f"v1 :{v1}")
print(type(v1))

print("-" * 60)
v2 = (x ** 2 for x in range(1, 11))                 # generator
print(f"v2 :{v2}")
print(type(v2))
print(v2.__next__())
print(v2.__next__())
print(v2.__next__())
print(v2.__next__())

print("-" * 60)
res1 = sum([x ** 2 for x in range(1, 11)])
print(f"res1 :{res1}")

res2 = sum((x ** 2 for x in range(1, 11)))
print(f"res2 :{res2}")

print("-" * 60)
exp1 = [x ** 2 for x in range(1, 1000)]
exp2 = (x ** 2 for x in range(1, 1000))

print(f"Comprehension size of list :{getsizeof(exp1)}")
print(f"Generator size of list :{getsizeof(exp2)}")
