import sys

print(sys.path)

# 如果在mod1路径下执行 python test1.py 是可以的
# import mod2.test2
# import mod2.mod3.test3
# 此种也可以
# from mod2 import test2
# from mod2.mod3 import test3

# 如果在mod1上层路径执行 python -m mod1.test1 需要使用以下
# 如果在mod1路径下执行 python test1.py 是报错的
# 因为如果想要直接执行一个py文件的时候，该文件中是不能有相对引入的
# .表明这就是相对引入
from .mod2 import test2
from .mod2.mod3 import test3


print('test1')