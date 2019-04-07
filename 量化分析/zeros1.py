import numpy as np
import pandas as pd

# 二维ndarray创建
data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'hello'), (2, 3., 'world')]
# print(data)
df = pd.DataFrame(data, index=['first', 'second'], columns=['C', 'A', 'B'])
# print(df)


# series组成的字典形式创建
data = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two': pd.Series([1., 2., 3.], index=['a', 'b', 'c'])}

df = pd.DataFrame(data, index=['d', 'b', 'a'], columns=['three', 'two'])

# print(df)

# 字典的列表形式创建
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
# print(df)

# 字典的字典形势创建
data = {
    ('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
    ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
    ('a', 'c'): {('A', 'B'): 5, ('A', 'B'): 6},
    ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
    ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}
}

df = pd.DataFrame(data)
print(df)
