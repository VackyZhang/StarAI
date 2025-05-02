# 封装完整数据准备流程（读取 -> 预处理 -> 保存）
import os
import pandas as pd
from prepare.preprocessor import fill_missing
from config import base_config

def prepare_stock(symbol: str, overwrite=False) -> pd.DataFrame:
    raw_path = os.path.join(base_config["data_dir"], "raw", f"{symbol}.csv")
    out_path = os.path.join(base_config["data_dir"], "processed", f"{symbol}.csv")

    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Missing raw data file: {raw_path}")
    if os.path.exists(out_path) and not overwrite:
        return pd.read_csv(out_path, parse_dates=["date"], index_col="date")

    df = pd.read_csv(raw_path, parse_dates=["date"], index_col="date")
    df = fill_missing(df)
    df.to_csv(out_path)
    return df
