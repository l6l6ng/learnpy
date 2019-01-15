import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
# import sys
# import matplotlib


# 准备数据
# 我们的数据包含了1880年出生的婴儿及其数量。 我们已经知道我们有1,000条记录而且没有缺失值(所有值都是非空 non-null 的)。
# 我们还可以验证一下 "Names" 列仅包含了5个唯一的名字。
#
# 我们可以使用 dataframe 的 unique 属性找出 "Names" 列的所有唯一的(unique)的记录。

Location = r'./data/births1880.txt'
df = pd.read_csv(Location, names=['Names', 'Births'])

# 方法 1:
# print(df['Names'].unique())

# 如果你想把这些值打印出来:
# for x in df['Names'].unique():
#     print(x)

# 方法 2:
# print(df['Names'].describe())
#
# count     1000
# unique       5
# top        Bob
# freq       206
# Name: Names, dtype: object

# 因为每一个婴儿名字对应有多个值，我们需要把这几个值汇总起来这样一个婴儿名字就只出现一次了。
# 这意味着 1,000 行将变成只有 5 行。 我们使用 groupby 函数来完成这个动作。

# 创建一个 groupby 的对象
name = df.groupby('Names')

# 在 groupby 对象上执行求和(sum)的功能

df = name.sum()
# print(df)
#
# Names    Births
# Bob      106817
# Jessica   97826
# John      90705
# Mary      99438
# Mel      102319

# 分析数据
# 要找到最高出生率的婴儿名或者是最热门的婴儿名字，我们可以这么做。
# 将 dataframe 排序并且找到第一行

# 方法 1:
# print(df.sort_values(['Births'], ascending=False).head(1))

# 使用 max() 属性找到最大值
# 方法 2：

# print(df['Births'].max())

# 表现数据
# 我们可以将 Births 这一列标记在图形上向用户展示数值最大的点。 对照数据表，用户就会
# 有一个非常直观的画面 Bob 是这组数据中最热门的婴儿名字。

# Create graph
df['Births'].plot.bar()