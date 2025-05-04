"""
测试 prepare_stock.py 模块
"""

import os
import pandas as pd
from config import base_config
from data.download.download_stock import download_stock
from data.prepare.prepare_stock import prepare_stock


def test_prepare_stock(tmp_path):
    """
    下载模拟数据 → 清洗 → 验证 processed 文件生成成功
    """
    # 临时替换配置
    old_data_dir = base_config["data_dir"]
    old_source = base_config.get("data_source", "akshare")
    base_config["data_dir"] = str(tmp_path)
    base_config["data_source"] = "tushare"  # ✅ 强制使用 tushare 数据源

    symbol = "000001.SZ"
    start = "2023-01-05"
    end = "2023-01-10"

    # 下载数据
    csv_path = download_stock(symbol, start, end, overwrite=True)
    assert csv_path != ""

    # 运行清洗流程
    df_ready = prepare_stock(symbol, overwrite=True)
    assert not df_ready.empty
    assert set(["open", "close", "volume"]).issubset(df_ready.columns)

    # 验证 processed 文件存在
    processed_path = os.path.join(tmp_path, "processed", f"{symbol}.csv")
    assert os.path.exists(processed_path)

    # 恢复路径配置
    base_config["data_dir"] = old_data_dir
    base_config["data_source"] = old_source
