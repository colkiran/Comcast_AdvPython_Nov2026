
l1 = list(range(1, 6))
print(f"l1 :{l1}")
print(f"type(l1) :{type(l1)}")

# copy the elements of l1 to l2
l2 = l1             # shallow copy
# copies the address along with the data
print(f"l2 :{l2}")
print(f"type(l2): {type(l2)}")

# add some new values into l2
l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"After l2 :{l2}")
print(f"After l1 :{l1}")

print("-" * 60)
l3 = [10, 20, 30, 40, 50]
print(f"l3 :{l3}")
print(type(l3))

# copy the elements of l3 to l4
l4 = l3.copy()          # deep copy
# copies only the data
print(f"l4 :{l4}")

l4.extend([60, 70, 80, 90])
print(f"After l4 :{l4}")
print(f"After l3 :{l3}")

print("-" * 60)
print("-" * 60)

l5 = [1, 2, 3, [20, 40, 60],4, 5]
print(f"l5 :{l5}")

# copy the elements of l5 to l6
l6 = l5.copy()          # deep copy
print(f"l6 :{l6}")

l6[3].append(80)
l6[3].append(100)
l6[3].append(120)

print(f"After l6 :{l6}")
print(f"After l5 :{l5}")

print("-" * 60)
print("-" * 60)
from copy import deepcopy
l7 = [1, 2, [5, 10, 15], 3, 4, 5]
print(f"l7 :{l7}")

# copy the elements of l7 to l8
l8 = deepcopy(l7)           # deepcopy
print(f"l8 :{l8}")

l8[2].append(20)
l8[2].append(25)
l8[2].append(30)

print(f"After l8 :{l8}")
print(f"After l7 :{l7}")

