# tests/datasets/test_builder.py
import pytest
import pandas as pd
from datasets.builder import build_dataset
from datasets.configs.dataset_config import DATASET_CONFIG
import os

@pytest.fixture
def create_sample_csv(tmp_path):
    """创建模拟的 CSV 文件用于测试"""
    # 创建一个简单的 DataFrame
    data = {
        "date": pd.date_range(start="2023-01-01", periods=5, freq="D"),
        "open": [10, 10.5, 11, 11.5, 12],
        "close": [10.5, 11, 11.5, 12, 12.5]
    }
    df = pd.DataFrame(data)

    # 模拟文件路径
    dataset_dir = tmp_path / "data" / "processed" / "000001.SZ"
    dataset_dir.mkdir(parents=True, exist_ok=True)

    # 保存 train.csv, val.csv 和 test.csv 文件
    csv_paths = {}
    for split in ["train", "val", "test"]:
        csv_path = dataset_dir / f"{split}.csv"
        df.to_csv(csv_path, index=False)
        csv_paths[split] = csv_path

    # 配置数据目录（调整 DATASET_CONFIG 路径）
    DATASET_CONFIG["processed_dir"] = str(tmp_path / "data" / "processed")

    return csv_paths  # 返回文件路径

def test_build_dataset(create_sample_csv):
    """测试数据构建过程"""
    # 获取创建的 CSV 文件路径
    csv_paths = create_sample_csv

    # 调用构建数据集函数
    X_train, y_train, X_val, y_val = build_dataset("000001.SZ")

    # 检查返回数据的维度
    assert X_train.shape[0] > 0  # 确保训练集有数据
    assert X_val.shape[0] > 0    # 确保验证集有数据
    assert y_train.shape[0] == X_train.shape[0]  # 标签和特征的行数一致
    assert y_val.shape[0] == X_val.shape[0]      # 标签和特征的行数一致

    # 确保所有的 CSV 文件都已创建
    assert os.path.exists(csv_paths["train"])
    assert os.path.exists(csv_paths["val"])
    assert os.path.exists(csv_paths["test"])
