import os
# 包内引入
# 相对引入
import test22
# 绝对引入
from pkg1 import test23

print('----------------')
print(os.path.abspath(__file__))
print('test21')
print('----------------')