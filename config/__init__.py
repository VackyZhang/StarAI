# config/__init__.py
# 加载和统一管理所有 YAML 配置文件（base, strategy, backtest 等）
# 可通过 base_config、strategy_config 等变量直接引用
# 也支持 get_config('xxx') 动态访问配置

import os
import yaml

CONFIG_DIR = os.path.dirname(__file__)
CONFIG_FILES = ['base', 'strategy', 'backtest', 'trading', 'model']
configs = {}

def load_yaml_config(file_name: str) -> dict:
    path = os.path.join(CONFIG_DIR, f"{file_name}.yaml")
    if not os.path.exists(path):
        print(f"[config] Warning: config file not found: {file_name}.yaml")
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

# 自动加载所有配置文件
for name in CONFIG_FILES:
    configs[name] = load_yaml_config(name)

# 快捷访问
base_config = configs['base']
strategy_config = configs['strategy']
backtest_config = configs['backtest']
trading_config = configs['trading']
model_config = configs['model']

def get_config(name: str) -> dict:
    return configs.get(name, {})
