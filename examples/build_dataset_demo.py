import os
import pandas as pd
from datasets.builder import build_dataset
from datasets.configs.dataset_config import DATASET_CONFIG

def ensure_data_file(symbol="000001.SZ", splits=("train", "val", "test")):
    data_dir = DATASET_CONFIG["processed_dir"]
    for split in splits:
        symbol_dir = os.path.join(data_dir, symbol)
        os.makedirs(symbol_dir, exist_ok=True)

        file_path = os.path.join(symbol_dir, f"{split}.csv")
        if not os.path.exists(file_path):
            print(f"数据文件不存在，创建模拟数据文件: {file_path}")
            data = {
                "date": pd.date_range(start="2023-01-01", periods=5, freq="D"),
                "close": [10.5, 11.0, 12.5, 13.0, 14.5]
            }
            df = pd.DataFrame(data)
            df.to_csv(file_path, index=False)

# 确保所有必要的数据文件存在
ensure_data_file()

# 测试构建
symbol = "000001.SZ"
X_train, y_train, X_val, y_val = build_dataset(symbol)
print(f"✅ 数据集构建完成: {symbol}")
