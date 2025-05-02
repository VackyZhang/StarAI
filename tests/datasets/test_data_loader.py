"""
测试 datasets.loaders.data_loader 的加载功能
"""
import os
import pandas as pd
import pytest
from datasets.loaders.data_loader import load_dataset
from datasets.configs.dataset_config import DATASET_CONFIG

def test_load_dataset(tmp_path):
    # 模拟一个处理好的数据集路径：data/processed/000001.SZ/train.csv
    symbol = "000001.SZ"
    split = "train"
    dataset_dir = tmp_path / "processed" / symbol
    dataset_dir.mkdir(parents=True)

    df_sample = pd.DataFrame({
        "date": ["2022-01-01", "2022-01-02"],
        "open": [10.0, 10.1],
        "close": [10.5, 10.6]
    })
    csv_path = dataset_dir / f"{split}.csv"
    df_sample.to_csv(csv_path, index=False)

    # 修改配置路径为临时路径
    DATASET_CONFIG["processed_dir"] = str(tmp_path / "processed")

    df_loaded = load_dataset(name=symbol, split=split)
    assert not df_loaded.empty
    assert "open" in df_loaded.columns
    assert df_loaded.shape[0] == 2
