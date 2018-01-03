from functools import reduce


def square(x):
    return x * x


r = map(square, [1, 2, 3, 4, 5, 6, 7, 8, 9])

rr = list(r)

# ----------------------------------------------------


def add(x, y):
    return x + y


sum = reduce(add, [1, 2, 3, 4, 5])

# ----------------------------------------------------


def is_odd(n):
    return n % 2 == 1


list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

# ----------------------------------------------------

print(sorted([1, -12, 53, 15, -23, 111]))
print(sorted([1, -12, 53, 15, -23, 111], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
