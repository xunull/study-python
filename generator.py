g = (x * x for x in range(1, 11))
for temp in g:
    print(temp)


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# fib(10)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# for n in fib(10):
#     print(n)


# for 循环在每次循环的时候可以获取到每次yield的值，但是无法获取函数最后的返回值
# 返回值在StopIteration错误的value中
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
