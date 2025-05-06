quant_ai/
├── __init__.py                   # 初始化模块
├── config.py                     # 配置加载与管理
├── core/                         # 核心功能模块
│   ├── __init__.py
│   ├── backtest.py               # 回测模块
│   ├── execution.py              # 执行引擎
│   ├── report.py                 # 生成报告
│   └── strategy.py               # 策略模块
├── data/                         # 数据相关模块
│   ├── __init__.py
│   ├── datasource.py             # 数据源
│   ├── loader.py                 # 数据加载
│   └── preprocessor.py           # 数据预处理
├── risk/                         # 风险管理模块
│   ├── __init__.py
│   └── risk_manager.py           # 风险控制
└── trading/                      # 交易模块
    ├── __init__.py
    ├── broker_base.py            # 交易接口基类
    ├── jqdatasdk.py              # 聚宽数据接口
    └── mock.py                   # 模拟交易接口

