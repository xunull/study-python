import os

# No module named 'test32'
# import test32

from . import test32

# No module named 'pgk1'
# from pgk1 import test33

from .pkg1 import test33

# python test3.test31 以这种方式运行， 不能使用相对引入


print('----------------')
print(os.path.abspath(__file__))
print('test31')
print('----------------')