import numpy as np
import pandas as pd

# s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'], dtype='int8')

s = pd.Series(np.random.rand(4), index=['a', 'b', 'c', 'd'])
print(s.index)
print(s.values)
print(s[['a','b']])
print(s[:2])
