import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
# import sys
# import matplotlib

# 创建数据
# 我们用到的数据集将包括在1880年出生的，1,000个婴儿姓名以及对应的出生数量。
# 我们将会增加一些重复值因此你会看到相同的婴儿名字重复了多次。你可以设想同一
# 个婴儿名字重复多次是因为不同的医院针对同一个婴儿名字上报的不同的出生数量。
# 因此，如果两家医院对“Bob”这个名字上报出生数量，就会有两个数值。 我们先开始
# 创建一组随机的数值。

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']

# 使用上面的5个名字来创建一个有1,000个婴儿名字的随机列表，我们要做如下一些操作:
# 生成一个 0 到 4 之间的随机数
# 我们会用到 seed，randint, len, range 和 zip 这几个函数。

# 这将确保随机样本是可以被重复生成的。
# 这也意味着生成的随机样本总是一样的。

# seed(500) - 创建一个种子
#
# randint(low=0, high=len(names)) - 生成一个随机整数，介于 0 和 "names" 列表的长度之间。
# names[n] - 从 "names" 列表中选择索引值(index)为 n 的名字。
# for i in range(n) - 循环直到 i 等于 n，即: 1,2,3,....n。
# random_names = 从 names 列表中选在一个随机名字并执行 n 次 (Select a random name from the name list and do this n times.)

random.seed(500)
random_names = [names[random.randint(low=0, high=len(names))] for i in range(1000)]

#显示前10个名字
# print(random_names[:10])

# 生成介于 0 和 1000 之间的随机数

# 1880年，不同婴儿名字对应的出生数量
births = [random.randint(low=0, high=1000) for i in range(1000)]
# print(births[:10])

BabyDataSet = list(zip(random_names,births))

# 用 zip 函数把 names 和 births 这两个数据集合并在一起。

# print(BabyDataSet[:10])

# 我们基本上完成了数据集的创建工作。 现在我们要用 pandas 库将这个数据集导出到一个 csv 文件中。
#
# df 是一个 DataFrame对象。 你可以把这个对象理解为包含了 BabyDataset 的内容而格式非常象一个 sql
# 表格或者 Excel 的数据表。 让我们看看 df 中的内容。

df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
# print(df[:10])

# 将 dataframe 导出到一个 csv 文件中。 我们将导出文件命名为 births1880.csv。 导出 csv 文件的函
# 数是 to_csv。 除非你指定了其他的文件目录，否则导出的文件将保存在和 notebook 文件相同的位置。
# df.to_csv?
# 我们会使用的参数是 index 和 header。 将这两个参数设置为 False 将会防止索引(index)和列名
# (header names)被导出到文件中。 你可以试着改变这两个参数值来更好的理解这两个参数的作用。

df.to_csv('./data/births1880.txt', index=False, header=False)