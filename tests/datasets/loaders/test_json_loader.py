"""
测试 json_loader.py 模块：加载 JSON 数据为 DataFrame
"""

import pytest
import pandas as pd
from datasets.loaders.json_loader import load_dataset


@pytest.fixture
def create_sample_json(tmp_path):
    """创建 JSON 测试文件"""
    data = {
        "date": pd.date_range(start="2023-01-01", periods=3, freq="D"),
        "close": [10.5, 11.2, 12.1]
    }
    df = pd.DataFrame(data)

    json_path = tmp_path / "data" / "processed" / "000001.SZ" / "train.json"
    json_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_json(json_path, orient="records", date_format="iso")

    return json_path


def test_load_json_dataset(create_sample_json):
    """测试从 JSON 文件加载数据集"""
    from datasets.configs.dataset_config import DATASET_CONFIG
    DATASET_CONFIG["processed_dir"] = str(create_sample_json.parent.parent)

    df = load_dataset("000001.SZ", split="train")

    assert not df.empty
    assert "close" in df.columns
    assert "date" in df.index.names
