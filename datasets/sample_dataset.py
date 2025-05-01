# datasets/sample_dataset.py
# 用于将数据加载 + 技术指标封装为统一函数，提供完整预处理流程

from datasets.loader import load_csv
from datasets.features import add_technical_indicators

def get_prepared_data(symbol: str, start: str, end: str):
    df = load_csv(symbol, start, end)
    df = add_technical_indicators(df)
    return df
