quant_ai/
├── __init__.py          # 初始化模块
├── config.py            # 量化交易的全局配置文件
├── core/                # 核心模块（执行、策略、回测、报告等）
│   ├── __init__.py
│   ├── execution.py     # 执行引擎
│   ├── strategy.py      # 策略模块
│   ├── backtest.py      # 回测模块
│   └── report.py        # 报告生成模块
├── data/                # 数据处理（数据源、加载、预处理等）
│   ├── __init__.py
│   ├── preprocessor.py  # 数据预处理
│   ├── datasource.py    # 数据源（获取外部数据）
│   └── loader.py        # 数据加载（支持不同格式如 CSV、Parquet）
├── trading/             # 交易模块（券商接口、模拟交易）
│   ├── __init__.py
│   ├── broker_base.py   # 基础券商接口
│   ├── jqdatasdk.py     # 聚宽数据接口
│   └── mock.py          # 模拟交易接口
├── risk/                # 风控模块
│   ├── __init__.py
│   └── risk_manager.py  # 风险管理
├── utils/               # 工具模块（定时器、日志、可视化等）
│   ├── __init__.py
│   ├── timer.py         # 定时器
│   ├── logger.py        # 日志工具
│   └── visualizer.py    # 可视化工具
