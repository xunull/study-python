'''
测试变量的作用域
'''

globalvar = 'global 1111'


def test():
    var1 = 1
    var2 = 2

    def inner():
        # 在嵌套的函数中 global并不是上层函数的作用域
        # 全局作用域就是最外层的作用域
        global globalvar
        globalvar = 'global 2222'

        # 不是本块作用域的变量
        nonlocal var1
        var1 = 11
        # 并不是修改上层作用域的变量
        # 而是定义并赋值了一个var2
        var2 = 22

    print('test var1 value is {}'.format(var1))
    print('test var2 value is {}'.format(var2))
    inner()
    print('[after inner] test var1 value is {}'.format(var1))
    print('[after inner] test var2 value is {}'.format(var2))


def main():
    print('globalvar is {}'.format(globalvar))
    test()
    print('globalvar is {}'.format(globalvar))


if __name__ == '__main__':
    main()
