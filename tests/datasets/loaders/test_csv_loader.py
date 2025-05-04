"""
测试 csv_loader.py 模块：加载 CSV 文件为 DataFrame
"""

import pytest
import pandas as pd
from datasets.loaders.csv_loader import load_dataset


@pytest.fixture
def create_sample_csv(tmp_path):
    """创建一个简单的 CSV 文件，用于测试"""
    data = {
        "date": pd.date_range(start="2023-01-01", periods=5, freq="D"),
        "close": [10, 12, 14, 16, 18]
    }
    df = pd.DataFrame(data)

    # 创建目录结构：<tmp>/data/processed/000001.SZ/train.csv
    csv_path = tmp_path / "data" / "processed" / "000001.SZ" / "train.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_path, index=False)

    return csv_path


def test_load_csv_dataset(create_sample_csv):
    """测试从 CSV 文件加载数据集"""
    # 修改配置路径为包含 000001.SZ 的上一级目录
    from datasets.configs.dataset_config import DATASET_CONFIG
    DATASET_CONFIG["processed_dir"] = str(create_sample_csv.parent.parent)

    df = load_dataset("000001.SZ", split="train")

    assert not df.empty
    assert "close" in df.columns
    assert df.shape[0] == 5
    assert "date" in df.index.names
