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

