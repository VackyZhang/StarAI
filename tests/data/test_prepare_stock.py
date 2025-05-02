# 测试 prepare_stock 是否能正常处理数据
import os
from data.prepare.prepare_stock import prepare_stock
from config import base_config

def test_prepare_stock():
    symbol = "000001.SZ"
    processed_path = os.path.join(base_config["data_dir"], "processed", f"{symbol}.csv")
    df = prepare_stock(symbol, overwrite=False)
    assert not df.empty
    assert "close" in df.columns
    assert os.path.exists(processed_path)
