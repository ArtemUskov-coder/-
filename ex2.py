def f(x):
    if x == 1:
        return 1
    if x == 2:
        return 3
    if x > 2:
        return f(x - 1) * f(x - 2) + (x - 2)
print(f(5))
