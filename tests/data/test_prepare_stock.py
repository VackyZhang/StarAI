import os
from config import base_config
from data.prepare.prepare_stock import prepare_stock
from data.download.download_stock import download_stock

def test_prepare_stock(tmp_path):
    # 修改 data_dir 为临时目录（避免污染本地 data）
    base_config["data_dir"] = str(tmp_path)

    symbol = "000001.SZ"
    df_raw = download_stock(symbol, "2022-01-01", "2022-01-05")
    raw_path = tmp_path / "raw" / f"{symbol}.csv"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    df_raw.to_csv(raw_path, index=False)

    df_ready = prepare_stock(symbol, overwrite=True)
    assert not df_ready.empty
    assert "close" in df_ready.columns

    processed_path = tmp_path / "processed" / f"{symbol}.csv"
    assert processed_path.exists()
