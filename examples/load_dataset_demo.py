"""
示例脚本：演示如何加载 datasets 中处理后的股票数据集
"""
from datasets.loaders.data_loader import load_dataset

if __name__ == "__main__":
    symbol = "000001.SZ"
    split = "train"

    try:
        df = load_dataset(name=symbol, split=split)
        print(f"✅ 成功加载数据集: {symbol}/{split}")
        print(df.head())
    except FileNotFoundError as e:
        print(f"❌ 加载失败：{e}")
        print("请先确保 data/processed/000001.SZ/train.csv 文件存在。")
