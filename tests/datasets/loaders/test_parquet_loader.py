"""
测试 parquet_loader.py 模块：加载 Parquet 数据为 DataFrame
"""

import pytest
import pandas as pd
from datasets.loaders.parquet_loader import load_dataset


@pytest.fixture
def create_sample_parquet(tmp_path):
    """创建 Parquet 测试文件"""
    data = {
        "date": pd.date_range(start="2023-01-01", periods=3, freq="D"),
        "close": [10.5, 11.0, 12.5]
    }
    df = pd.DataFrame(data)

    parquet_path = tmp_path / "data" / "processed" / "000001.SZ" / "train.parquet"
    parquet_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(parquet_path, index=False)

    return parquet_path


def test_load_parquet_dataset(create_sample_parquet):
    """测试从 Parquet 文件加载数据集"""
    from datasets.configs.dataset_config import DATASET_CONFIG
    DATASET_CONFIG["processed_dir"] = str(create_sample_parquet.parent.parent)

    df = load_dataset("000001.SZ", split="train")

    assert not df.empty
    assert "close" in df.columns
    assert "date" in df.index.names
