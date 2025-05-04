# examples/load_dataset_demo.py

from datasets.loaders.csv_loader import load_dataset
from datasets.configs.dataset_config import DATASET_CONFIG

symbol = "000001.SZ"
split = "train"

try:
    df = load_dataset(symbol, split=split)
    print(df.head())
except FileNotFoundError as e:
    print(f"❌ 加载失败: {e}")
