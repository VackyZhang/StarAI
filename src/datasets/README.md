✅ 拆分的理由（适合中大型项目）：
职责更清晰：
data/ 是“获取和生成数据”，
datasets/ 是“让模型消费数据”。

适合团队分工：
数据工程师维护 data/，算法工程师使用 datasets/。
支持多个数据来源统一接口（如 CSV / Parquet / SQL / API）
方便后期对接 PyTorch Dataset / Tensorflow Dataset


# 📦 datasets

用于模型训练前的数据加载逻辑封装，包括 CSV -> DataFrame -> 模型输入等转换过程。

### 📁 子目录说明

- `loaders/`：加载处理好的数据（如 data/processed）为 DataFrame
- `configs/`：定义和加载数据路径、结构等配置


datasets/
├── __init__.py                            # 可空，用于标记包结构
├── builder.py                             # 主入口：组织加载、特征构造、拆分等流程
├── splitter.py                            # 拆分数据为 train/val/test 的工具
├── features.py                            # 特征构造，如添加技术指标、滑窗等
│
├── loaders/                               # 数据加载子模块：支持 CSV、Parquet、SQL
│   ├── __init__.py
│   ├── csv_loader.py                      # ✅ 实现：从 data/processed 加载 CSV
│   ├── parquet_loader.py                  # 🔲 预留：从 Parquet 加载数据
│   └── sql_loader.py                      # 🔲 预留：从数据库（如 ClickHouse）加载
│
├── configs/                               # 数据集相关配置（不依赖主 config/）
│   ├── __init__.py
│   ├── dataset_config.py                  # ✅ 实现：加载 dataset_config.yaml
│   └── dataset_config.yaml                # ✅ 示例：指定 processed_dir、raw_dir 等
