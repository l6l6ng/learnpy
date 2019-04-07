import numpy as np
import pandas as pd

# serier 数据对象的生成
# s = pd.Series([1, 2, 3, 4, 5],index=['a', 'b', 'c', 'd', 'e'])
s = pd.Series(np.random.randn(5),index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s.index)
print(s.values)
print(s[:2])
