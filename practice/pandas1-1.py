import pandas as pd

Location = r'./data/birth1880.csv'

df = pd.read_csv(Location, names=['Names', 'Births'])

# print(df)

# import os
# os.remove(Location)

# print(df.dtypes)

# print(df.Births.dtypes)

# 分析数据
# 要找到最高出生率的婴儿名或者是最热门的婴儿名字，我们可以这么做。
# 将 dataframe 排序并且找到第一行
# 使用 max() 属性找到最大值

#方法1：
# Sorted = df.sort_values(['Births'], ascending=False)
# print(Sorted.head(1))

#方法2：
# print(df['Births'].max())

# 表现数据
# 我们可以将 Births 这一列标记在图形上向用户展示数值最大的点。 对照数据表，用户就会有一个非常直观的画面 Mel 是这组数据中最热门的婴儿名字。
# pandas 使用非常方便的 plot() 让你用 dataframe 中的数据来轻松制图。 刚才我们在 Births 列找到了最大值，现在我们要找到 973 这个值对应的婴儿名字。
# 每一部分的解释:
# df['Names'] - 这是完整的婴儿名字的列表，完整的 Names 列
# df['Births'] - 这是1880年的出生率，完整的 Births 列
# df['Births'].max() - 这是 Births 列中的最大值
# [df['Births'] == df['Births'].max()] 的意思是 [在 Births 列中找到值是 973 的所有记录]
# df['Names'][df['Births'] == df['Births'].max()] 的意思是 在 Names 列中挑选出 [Births 列的值等于 973] (Select all of the records in the Names column WHERE [The Births column is equal to 973])
# 一个另外的方法是我们用过 排序过的 dataframe: Sorted['Names'].head(1).value
# str() 可以将一个对象转换为字符串。

# print(df['Names'][df['Births'] == df['Births'].max()])

# print(df.sort_values(['Births'], ascending=False).head(1))

# 绘图
# df['Births'].plot()
df['Births'].plot.bar()  #这里改用的条形图更直观