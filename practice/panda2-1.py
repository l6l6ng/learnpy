import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
# import sys
# import matplotlib

# 我们将使用 pandas 的 read_csv 函数从 csv 文件中获取数据。 我们先看看这个函数的帮助以及它需要什么参数。
#
# pd.read_csv?
# 这个函数有很多的参数，但我们目前只需要文件的位置。
# 注意: 取决于你把 notebook 保存在什么位置，你也许需要修改一下文件的位置。

Location = r'./data/births1880.txt'
df = pd.read_csv(Location, names=['Names', 'Births'])

# 注意字符串之前的 r 。 因为斜线(slash)是一个特殊字符，在字符串之前放置前导的 r 将会把整个字符串进行转义(escape)

# print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 999 entries, 0 to 998
# Data columns (total 2 columns):
# Mary    999 non-null object
# 968     999 non-null int64
# dtypes: int64(1), object(1)
# memory usage: 15.7+ KB

# 汇总信息:
# 数据集里有 999 条记录
# 有一列 Mary 有 999 个值
# 有一列 968 有 999 个值
# 这两列, 一个是numeric(数字型), 另外一个是non numeric(非数字型)
# 我们可以使用 head() 这个函数查看一下dataframe中的前 5 条记录。 你也可以传入一个数字 n 来查看 dataframe 中的前 n 条记录。

# print(df.head(5))

# 让我们看一下这个 dataframe 的最后 5 条记录。

# print(df.tail(5))

# 你可以把数字 [0,1,2,3,4] 设想为 Excel 文件中的行标 (row number)。 在 pandas 中，这些是 索引 (index) 的一部分。 你可以把索引
# (index)理解为一个sql表中的主键(primary key)，但是索引(index)是可以重复的。
#
# [Names, Births] 是列名，和sql表或者Excel数据表中的列名(column header)是类似的。