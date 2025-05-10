# tests/quant_ai/data/test_loader.py

import os
import pytest
import pandas as pd
from quant_ai.data.loader import DataLoader
from common.file_utils import save_csv, save_json

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "date": pd.date_range("2023-01-01", periods=3),
        "value": [10, 20, 30]
    })

def test_load_csv(tmp_path, sample_df):
    path = tmp_path / "test.csv"
    save_csv(sample_df, path)
    loader = DataLoader()
    df = loader.load(path, fmt="csv", index_col=None)

    # 统一字符串格式以避免 datetime 精度差异
    df["date"] = df["date"].astype(str)
    expected = sample_df.copy()
    expected["date"] = expected["date"].astype(str)

    assert df.equals(expected)

def test_load_json(tmp_path, sample_df):
    path = tmp_path / "test.json"
    save_json(sample_df.to_dict(orient="records"), path)
    loader = DataLoader()
    df = loader.load(path, fmt="json")

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(sample_df)
    assert set(df.columns) == set(sample_df.columns)

def test_load_dataframe(sample_df):
    loader = DataLoader()
    df = loader.load(sample_df, fmt="dataframe")
    assert df.equals(sample_df)

def test_load_invalid_format(sample_df):
    loader = DataLoader()
    with pytest.raises(ValueError):
        loader.load(sample_df, fmt="unknown")

def test_load_non_dataframe_as_dataframe():
    loader = DataLoader()
    with pytest.raises(TypeError):
        loader.load("not a df", fmt="dataframe")
