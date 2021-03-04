import hashlib
import pandas as pd

str = 'abc123'
# md5.update(str.encode(encoding='utf-8'))
# print(md5.hexdigest())

def get_md5(str):
    return hashlib.md5(str.encode()).hexdigest()