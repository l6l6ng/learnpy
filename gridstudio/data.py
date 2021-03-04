import numpy as np
import pandas as pd
import os
import sys
# import md5
import json
import hashlib


# import md5


def get_md5(str):
    return hashlib.md5(str.encode()).hexdigest()


# path = os.getcwd() + '/gridstudio/data/project_object_fill_values.xlsx'
path = '/Users/liulong/workspace/郑州/新增账号0303.xlsx'
# path = '/Users/liulong/workspace/郑州/发刘龙/3-账号/2021年郑州市成果奖评审申报账号清单20210218.xlsx'
data = pd.read_excel(path, index_col=None, header=0)

print(data)

for i in range(data['密码'].size):
    md5 = get_md5(str(data['密码'][i]))
    # data['md5'][i] = md5
    data.loc[i, 'md5'] = md5
    # a = data['content'][i]
    # a = '中文'
    # data['c'][i] = a.encode("unicode_escape")
    # data['c'][i] = json.dumps(a).strip('"')
print(data)
data.to_excel(path, index=False)

# print(True)
