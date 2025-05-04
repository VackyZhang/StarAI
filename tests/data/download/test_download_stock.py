"""
测试 download_stock.py 模块，验证股票数据下载流程。
"""

import os
import pandas as pd
from data.download.download_stock import download_stock
from config import base_config


def test_download_stock(tmp_path):
    """
    使用 tushare 作为数据源，下载股票并验证保存 + 内容结构。
    """
    old_data_dir = base_config["data_dir"]
    old_source = base_config.get("data_source", "akshare")

    base_config["data_dir"] = str(tmp_path)
    base_config["data_source"] = "tushare"  # ✅ 切换数据源为 tushare

    symbol = "000001.SZ"
    start = "2023-01-05"
    end = "2023-01-10"

    csv_path = download_stock(symbol, start, end, overwrite=True)
    assert csv_path != "", "下载返回路径为空"
    assert os.path.exists(csv_path), f"文件未生成: {csv_path}"

    df = pd.read_csv(csv_path)
    assert not df.empty, "CSV 内容为空"
    assert set(["open", "high", "low", "close", "volume"]).issubset(df.columns)

    # 恢复原配置，避免影响其他测试
    base_config["data_dir"] = old_data_dir
    base_config["data_source"] = old_source
