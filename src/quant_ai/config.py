# quant_ai/config.py

"""
配置管理模块：加载和管理量化交易框架的所有配置文件，包括回测配置、模型配置等。
"""

import os
from common.config_loader import load_yaml_config
from common.paths import CONFIG_DIR
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 配置文件路径
BASE_CONFIG_PATH = os.path.join(CONFIG_DIR, "base.yaml")
STRATEGY_CONFIG_PATH = os.path.join(CONFIG_DIR, "strategy.yaml")
BACKTEST_CONFIG_PATH = os.path.join(CONFIG_DIR, "backtest.yaml")
TRADING_CONFIG_PATH = os.path.join(CONFIG_DIR, "trading.yaml")
MODEL_CONFIG_PATH = os.path.join(CONFIG_DIR, "model.yaml")
RISK_CONFIG_PATH = os.path.join(CONFIG_DIR, "risk.yaml")

# 加载各配置文件
base_config = load_yaml_config(BASE_CONFIG_PATH)
strategy_config = load_yaml_config(STRATEGY_CONFIG_PATH)
backtest_config = load_yaml_config(BACKTEST_CONFIG_PATH)
trading_config = load_yaml_config(TRADING_CONFIG_PATH)
model_config = load_yaml_config(MODEL_CONFIG_PATH)
risk_config = load_yaml_config(RISK_CONFIG_PATH)

def get_config(config_name: str):
    """
    根据配置名称获取相应的配置字典。

    参数:
        config_name (str): 配置名称（如 'base', 'strategy', 'backtest' 等）

    返回:
        dict: 配置字典
    """
    config_map = {
        "base": base_config,
        "strategy": strategy_config,
        "backtest": backtest_config,
        "trading": trading_config,
        "model": model_config,
        "risk": risk_config
    }
    return config_map.get(config_name, {})
