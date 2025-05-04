# StarAI  
AI-driven Quantitative Trading Framework

---

## 🚀 Features

- **Modular architecture**  
  - `src/common/` 通用工具、日志、路径管理、配置加载  
  - `src/config/` YAML + `.env` 配置管理  
  - `src/data/` 数据下载与预处理逻辑  
  - `src/datasets/` 训练前数据加载、拆分、特征构造  
  - `src/quant_ai/` 策略、回测、执行、风控核心业务  
- **Data pipeline**  
  - 原始数据 → 中间清洗 → 最终特征  
- **Pluggable data sources**  
  - 支持 AkShare、Tushare  
- **Easy to extend**  
  - 在 `common/` 中即可添加全局工具  
  - 在 `quant_ai/` 中可新增策略、引擎、券商适配器  

---

## 🚚 Installation

```bash
git clone https://github.com/VackyZhang/StarAI.git
cd StarAI

# 创建并激活虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install --upgrade pip
pip install -r requirements.txt

# 安装项目包
pip install -e .
