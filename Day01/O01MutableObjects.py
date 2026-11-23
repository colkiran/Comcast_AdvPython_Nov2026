
# mutable objects
# 1. list
l1 = list()
print(f"l1 :{l1}")
print(f"type(l1) :{type(l1)}")

print("-" * 60)
l2 = [1, 2, 3, 4, 5]
print(f"l2 :{l2}")
print(f"type(l2) :{type(l2)}")

print("-" * 60)
l3 = [1, 2, 3, 4, 5, 'six', 'seven', 'eight', 9.1, 10.3, 11.05, True, False]
print(f"l3 :{l3}")
print(f"type(l3 :{l3}")

print("-" * 60)
l1 = list(range(1, 11))
print(f"l1 :{l1}")

# immutable means we can change the value of the object after creation
l1[1] = 20
l1[-1] = 100
print(f"l1 :{l1}")

print("dictionary".center(60, "-"))
d1 = dict()
print(f"d1 :{d1}")
print(f"type(d1): {type(d1)}")

print("-" * 60)
d2 = {'name': 'Sachin', 'age': 34, 'runs': 85}
print(f"d2 :{d2}")
print(f"type(d2): {type(d2)}")

print("-" * 60)
d3 = dict([('name', 'sachin'), ('age', 34), ('runs', 120)])
print(f"d3 :{d3}")
print(f"type(d3): {type(d3)}")

print("-" * 60)
d4 = dict(name="sachin", age=34, runs=102)
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
player = {'name': 'Sachin', 'age': 32, 'runs': 92, 'oppn': 'Aus'}
print(f"player :{player}")
print(f"Name :{player['name']}")
print(f"Age  :{player['age']}")
print(f"Runs :{player['runs']}")
player['name'] = "Tendulkar"
player['venue'] = 'Gaba'
print(f"player :{player}")

print("set".center(60, "-"))
# elements of a set is always unique
s1 = {1, 2, 3, 4, 5.1, 6.2, 7.8, 'eight', 'nine', 'ten', True, False}
print(f"s1 :{s1}")
print(f"type(s1): {type(s1)}")
