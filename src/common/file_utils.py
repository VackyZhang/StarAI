"""
文件工具模块：封装常用的数据文件读取与保存操作，支持 CSV / JSON / Pickle / Parquet。
"""

import os
import json
import pickle
import pandas as pd
from common.paths import ensure_dir


def save_csv(df: pd.DataFrame, path: str, index: bool = False, encoding: str = "utf-8") -> None:
    """保存 DataFrame 为 CSV 文件"""
    ensure_dir(os.path.dirname(path))
    df.to_csv(path, index=index, encoding=encoding)


def load_csv(path: str, index_col: int | str | None = None, encoding: str = "utf-8") -> pd.DataFrame:
    """加载 CSV 文件为 DataFrame"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"找不到文件: {path}")
    return pd.read_csv(path, index_col=index_col, encoding=encoding)


def save_json(obj: dict, path: str, indent: int = 2, ensure_ascii: bool = False) -> None:
    """保存对象为 JSON 文件"""
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=indent, ensure_ascii=ensure_ascii)


def load_json(path: str) -> dict:
    """加载 JSON 文件为 Python 对象"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"找不到文件: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_pickle(obj: object, path: str) -> None:
    """保存对象为二进制 pickle 文件"""
    ensure_dir(os.path.dirname(path))
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(path: str) -> object:
    """加载 pickle 文件为对象"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"找不到文件: {path}")
    with open(path, "rb") as f:
        return pickle.load(f)


def save_parquet(df: pd.DataFrame, path: str, index: bool = False) -> None:
    """保存 DataFrame 为 Parquet 文件"""
    ensure_dir(os.path.dirname(path))
    df.to_parquet(path, index=index)


def load_parquet(path: str) -> pd.DataFrame:
    """加载 Parquet 文件为 DataFrame"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"找不到文件: {path}")
    return pd.read_parquet(path)
