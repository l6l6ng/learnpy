import pandas as pd

# 列表组成的字典形式创建
df = pd.DataFrame({'one': [1., 2, 3, 5], 'two': [1, 2, 3, 4]})
# print(df)

# 以嵌套列表的形式创建
df = pd.DataFrame([[1., 2, 3., 5], [1, 2, 3, 5]], index=['a', 'b'], columns=['one', 'two', 'three', 'four'])
print(df)
# print(df.index)
# print(df.columns)
# print(df.values)
# print(df['one'])
# print(df[:1])
print(df.loc[:, ['one', 'two']])
print(df.loc[['a'], ['one']])
