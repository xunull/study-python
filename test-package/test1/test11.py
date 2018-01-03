import os
# 在这里是可以引入test2，在当前执行的文件夹是在python 的path中的，每个文件都相当于一个模块
import test2

print('----------------')
print(os.path.abspath(__file__))
print('test11')
print('----------------')