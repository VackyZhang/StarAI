# datasets/loader.py
# 用于加载本地 CSV 数据文件，可按 symbol 和日期范围读取数据

import pandas as pd
import os
from config import base_config

def load_csv(symbol: str, start=None, end=None):
    path = os.path.join(base_config['data_dir'], 'raw', f'{symbol}.csv')
    df = pd.read_csv(path, parse_dates=['date'], index_col='date')
    if start:
        df = df[df.index >= pd.to_datetime(start)]
    if end:
        df = df[df.index <= pd.to_datetime(end)]
    return df.sort_index()
