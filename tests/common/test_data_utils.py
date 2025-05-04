"""
测试 data_utils.py：验证缺失值填充逻辑、CSV 保存功能是否正常。
"""

import os
import pandas as pd
from common.data_utils import fill_missing, save_dataframe

def test_fill_missing_ffill():
    df = pd.DataFrame({"A": [1, None, 3]})
    filled = fill_missing(df, method="ffill")
    assert filled.isnull().sum().sum() == 0
    assert filled.iloc[1]["A"] == 1  # 前向填充

def test_fill_missing_bfill():
    df = pd.DataFrame({"A": [None, 2, None]})
    filled = fill_missing(df, method="bfill")
    # 后向填充只能填 index 0，index 2 因为后面没值依然是 NaN
    assert filled.iloc[0]["A"] == 2
    assert pd.isna(filled.iloc[2]["A"])  # 第 2 行填不动

def test_fill_missing_mean():
    df = pd.DataFrame({"A": [1, None, 3]})
    filled = fill_missing(df, method="mean")
    assert filled.isnull().sum().sum() == 0
    assert filled.iloc[1]["A"] == 2  # 均值填充

def test_fill_missing_median():
    df = pd.DataFrame({"A": [1, None, 100]})
    filled = fill_missing(df, method="median")
    assert filled.isnull().sum().sum() == 0
    assert filled.iloc[1]["A"] == 50.5  # 中位数填充

def test_fill_missing_mode():
    df = pd.DataFrame({"A": [7, None, 7, 9]})
    filled = fill_missing(df, method="mode")
    assert filled.isnull().sum().sum() == 0
    assert filled.iloc[1]["A"] == 7  # 众数填充

def test_fill_missing_invalid_method():
    df = pd.DataFrame({"A": [1, None, 2]})
    try:
        fill_missing(df, method="invalid")
    except ValueError as e:
        assert "不支持的填充方法" in str(e)

def test_save_dataframe(tmp_path):
    df = pd.DataFrame({"A": [1, 2, 3]})
    out_path = tmp_path / "test" / "output.csv"
    save_dataframe(df, str(out_path), index=False)

    assert out_path.exists()
    loaded = pd.read_csv(out_path)
    assert loaded.shape == (3, 1)
    assert list(loaded.columns) == ["A"]
