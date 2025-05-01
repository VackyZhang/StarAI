# data/prepare.py
# 数据准备入口，包含清洗、合并、缺失值处理等操作，用于生成 processed 数据

import pandas as pd
import os
from datasets.preprocessor import fill_missing
from config import base_config

def prepare_stock(symbol: str, overwrite=False):
    raw_path = os.path.join(base_config['data_dir'], 'raw', f'{symbol}.csv')
    out_path = os.path.join(base_config['data_dir'], 'processed', f'{symbol}.csv')

    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Missing raw file: {raw_path}")
    
    if os.path.exists(out_path) and not overwrite:
        print(f"[Prepare] Using existing processed file: {out_path}")
        return pd.read_csv(out_path)

    df = pd.read_csv(raw_path, parse_dates=['date'], index_col='date')
    df = fill_missing(df)
    df.to_csv(out_path)
    print(f"[Prepare] Processed {symbol} saved to {out_path}")
    return df
