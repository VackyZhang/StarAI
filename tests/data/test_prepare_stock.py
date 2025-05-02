"""
测试 prepare_stock 是否能正常处理数据并保存到 processed 路径下
"""
import os
from config import base_config
from data.prepare.prepare_stock import prepare_stock
from data.download.download_stock import download_stock

def test_prepare_stock(tmp_path):
    # 设置 config 中的数据目录为 pytest 临时目录
    base_config["data_dir"] = str(tmp_path)

    symbol = "000001.SZ"
    start, end = "2022-01-01", "2022-01-05"

    # 下载测试数据并保存到 raw 目录
    df_raw = download_stock(symbol, start, end)
    raw_path = tmp_path / "raw" / f"{symbol}.csv"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    df_raw.to_csv(raw_path, index=False)

    # 🔧 显式创建 processed 目录，避免写入时失败
    processed_path = tmp_path / "processed"
    processed_path.mkdir(parents=True, exist_ok=True)

    # 执行数据预处理
    df_ready = prepare_stock(symbol, overwrite=True)

    # 断言处理结果存在且字段完整
    assert not df_ready.empty
    assert "close" in df_ready.columns
    assert (tmp_path / "processed" / f"{symbol}.csv").exists()
