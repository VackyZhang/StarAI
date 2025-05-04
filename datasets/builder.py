# datasets/builder.py
from datasets.loaders.csv_loader import load_dataset
import pandas as pd

def build_dataset(symbol: str) -> tuple:
    """
    构建训练集和验证集，并返回相应的特征和标签。
    """
    # 如果是 "all"，将其分解为 train, val, test
    splits = ["train", "val", "test"]

    # 加载各个切分的数据集
    datasets = [load_dataset(symbol, split=split) for split in splits]

    # 合并数据集
    df = pd.concat(datasets, axis=0)

    # 特征和标签处理
    X = df.drop(columns=["close"])  # 假设 "close" 是我们要预测的目标列
    y = df["close"]

    # 划分训练集和验证集
    train_size = int(0.8 * len(X))  # 80% 用于训练
    X_train, X_val = X[:train_size], X[train_size:]
    y_train, y_val = y[:train_size], y[train_size:]

    return X_train, y_train, X_val, y_val
