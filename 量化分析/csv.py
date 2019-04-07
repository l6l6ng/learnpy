import numpy as np
import pandas as pd

df_csvload = pd.read_csv('./fzcm.csv', parse_dates=True, index_col=0, encoding='utf8')
# print(df_csvload)

# print(df_csvload.head(3))
# print(df_csvload.tail(3))

# print(df_csvload.shape)

# print(df_csvload.describe())
# print(df_csvload.info())

print(df_csvload.head(5))