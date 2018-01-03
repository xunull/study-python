# python test41
# python pkg1/test41.py
# python -m pkg1.test41
# 都会报错
# attempted relative import beyond top-level package

# python -m test4.pkg1.test41
# 在整个包的最外面执行可以

from ..pkg2 import test42




print('test41')