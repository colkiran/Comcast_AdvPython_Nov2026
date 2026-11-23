# Pass by value
# pass by reference

# mutable object as argument
def result(marks):
    marks.append(85)

lst = [90, 93, 75]
print(f"before lst :{lst}")

result(lst)
print(f"after lst :{lst}")


print("-" * 60)
# immutable object as argument
def fun(x):
    print(f"x :{x}")
    x += 20
    print(F"After modification x: {x}")

n = 50
print(f"n before the function call :{n}")

fun(n)
print(f"n after the function call: {n}")
