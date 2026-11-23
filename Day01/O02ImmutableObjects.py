
# immutable objects
print("Integers".center(60, "-"))
x = 10
print(f"x :{x}")
print(f"type(x) :{type(x)}")
print(id(x))

x = x + 10
print(f"x :{x}")
print(id(x))

print("string".center(60, "-"))
st = "hello world"
print(f"st: {st}")
print(f"type(st) :{type(st)}")
print(f"st[6] :{st[6]}")
# st[6] = "W"
# st = "Hello World"

print("tuple".center(60, "-"))
# tuples are immutable lists
t1 = tuple()
print(f"t1 :{t1}")
print(f"type(t1): {type(t1)}")

print("-" * 60)
t2 = tuple(range(1, 6))
print(f"t2: {t2}")
print(f"t2[2] :{t2[2]}")
# t2[2] = 300

print("frozenset".center(60, "-"))
fs1 = frozenset((1, 2, 3, 4, 5))
print(f"fs1 :{fs1}")
print(f"type(fs1): {type(fs1)}")
#
# s1 = {10, 20, 30}
# print(f"s1 :{s1}")
# print(type(s1))
