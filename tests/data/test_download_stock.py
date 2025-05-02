from data.download.download_stock import download_stock
import pandas as pd

def test_download_stock():
    df = download_stock("000001.SZ", "2022-01-01", "2022-01-05")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "open" in df.columns
    assert df.shape[0] > 0
