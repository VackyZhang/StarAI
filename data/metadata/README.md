project_root/
├── data/                         # 所有数据输出的根目录
│   ├── raw/                      # 原始数据（不可变，作为源头）
│   │   ├── market/               # 市场行情数据
│   │   │   ├── 000001.SZ.csv
│   │   │   ├── spy_2023.csv
│   │   │   └── …
│   │   └── fundamental/          # 基本面、财务报表等
│   ├── interim/                  # 中间文件（简单清洗、合并后的数据）
│   │   ├── market_cleaned.parquet
│   │   └── …
│   ├── processed/                # 最终训练／回测用的特征集
│   │   ├── 000001.SZ/            # 按符号／品种拆分子目录
│   │   │   ├── train.csv
│   │   │   ├── val.csv
│   │   │   └── test.csv
│   │   └── aapl_features.parquet
│   ├── external/                 # 第三方下载的依赖文件（如行业分类、基准收益）
│   └── metadata/                 # 元数据（schema 定义、数据字典、版本说明）
│       └── README.md             # 说明哪些文件、格式如何使用
