"""
测试 file_utils.py：验证数据保存与加载（CSV/JSON/Pickle）。
"""

import os
import pandas as pd
from common.file_utils import (
    save_csv, load_csv,
    save_json, load_json,
    save_pickle, load_pickle,
)


def test_save_and_load_csv(tmp_path):
    df = pd.DataFrame({"A": [1, 2]})
    file_path = tmp_path / "subdir" / "data.csv"
    save_csv(df, str(file_path))

    assert file_path.exists()
    df2 = load_csv(str(file_path))
    assert df2.shape == (2, 1)
    assert list(df2.columns) == ["A"]


def test_save_and_load_json(tmp_path):
    obj = {"a": 1, "b": {"c": 2}}
    path = tmp_path / "config.json"
    save_json(obj, str(path))
    assert path.exists()

    loaded = load_json(str(path))
    assert loaded["b"]["c"] == 2


def test_save_and_load_pickle(tmp_path):
    data = {"x": [1, 2, 3]}
    path = tmp_path / "model.pkl"
    save_pickle(data, str(path))

    assert path.exists()
    obj = load_pickle(str(path))
    assert obj["x"] == [1, 2, 3]


def test_load_missing_file_raises(tmp_path):
    missing_path = tmp_path / "not_found.csv"
    try:
        load_csv(str(missing_path))
    except FileNotFoundError as e:
        assert "找不到文件" in str(e)
