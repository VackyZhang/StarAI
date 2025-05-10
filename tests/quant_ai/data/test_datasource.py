# tests/quant_ai/data/test_datasource.py

import pandas as pd
import pytest
from unittest.mock import patch, MagicMock
from quant_ai.data.datasource import DataSource

@patch("quant_ai.data.datasource.download_stock")
@patch("pandas.read_csv")
def test_get_data_success(mock_read_csv, mock_download_stock, tmp_path):
    # 模拟 CSV 文件路径
    dummy_path = tmp_path / "mock.csv"
    dummy_path.write_text("date,price\n2023-01-01,100\n2023-01-02,101")

    mock_download_stock.return_value = str(dummy_path)
    mock_read_csv.return_value = pd.DataFrame({
        "date": pd.to_datetime(["2023-01-01", "2023-01-02"]),
        "price": [100, 101]
    })

    source = DataSource()
    df = source.get_data("000001.SZ", "2023-01-01", "2023-01-02")

    assert not df.empty
    assert "price" in df.columns
    assert df.index.name == "date"

@patch("quant_ai.data.datasource.download_stock")
def test_get_data_empty_path(mock_download_stock):
    mock_download_stock.return_value = ""
    source = DataSource()
    df = source.get_data("FAKE", "2023-01-01", "2023-01-02")
    assert df.empty

@patch("quant_ai.data.datasource.download_stock")
@patch("pandas.read_csv")
def test_get_data_read_csv_error(mock_read_csv, mock_download_stock):
    mock_download_stock.return_value = "/fake/path.csv"
    mock_read_csv.side_effect = Exception("read_csv failed")

    source = DataSource()
    df = source.get_data("000001.SZ", "2023-01-01", "2023-01-02")
    assert df.empty
