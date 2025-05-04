project_root/
├── data/                   # 一切“数据文件”都集中在这里
│   ├── raw/                # 原始下载的快照
│   ├── interim/            # 中间产物（如清洗后的 Parquet）
│   ├── processed/          # 最终训练/回测数据
│   ├── external/           # 第三方依赖文件（行业分类、基准收益等）
│   └── metadata/           # 数据字典、schema 说明
├── models/                 # 模型权重和检查点
│   ├── checkpoints/
│   ├── final/
│   └── logs/
├── logs/                   # 运行、回测、数据管道日志
├── src/                    # 纯代码包（common、config、data、datasets、quant_ai）
├── tests/                  # 单元/集成测试
├── examples/               # 示例脚本
├── docs/                   # 文档
├── scripts/                # 运维/调度脚本
├── .github/                # CI 配置
├── .env/.gitignore 等      # 环境／VCS 配置
└── setup.py, requirements.txt, pytest.ini, print_structure.py, README.md…
