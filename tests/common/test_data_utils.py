"""
测试 data_utils.py：验证缺失值填充、归一化、标准化等函数。
"""

import pandas as pd
from common.data_utils import fill_missing, normalize, standardize


def test_fill_missing_mean():
    df = pd.DataFrame({"A": [1, None, 3]})
    filled = fill_missing(df, method="mean")
    assert filled.isnull().sum().sum() == 0
    assert filled.iloc[1]["A"] == 2


def test_fill_missing_mode():
    df = pd.DataFrame({"A": [7, None, 7, 9]})
    filled = fill_missing(df, method="mode")
    assert filled.iloc[1]["A"] == 7


def test_fill_missing_invalid():
    df = pd.DataFrame({"A": [1, None, 2]})
    try:
        fill_missing(df, method="bad")
    except ValueError as e:
        assert "不支持的填充方法" in str(e)


def test_normalize():
    df = pd.DataFrame({"A": [1, 2, 3]})
    result = normalize(df, ["A"])
    assert result["A"].min() == 0
    assert result["A"].max() == 1


def test_standardize():
    df = pd.DataFrame({"A": [1, 2, 3]})
    result = standardize(df, ["A"])
    assert abs(result["A"].mean()) < 1e-6
