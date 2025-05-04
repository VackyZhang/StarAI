"""
build_dataset_demo.py

示例脚本：演示如何使用 datasets.builder 构建训练数据集。
"""

from datasets.builder import build_dataset

symbol = "000001.SZ"

X_train, y_train, X_val, y_val = build_dataset(symbol)

print(f"Train Shape: {X_train.shape}, {y_train.shape}")
print(f"Val Shape: {X_val.shape}, {y_val.shape}")
