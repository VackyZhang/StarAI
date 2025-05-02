"""
配置管理模块：统一加载项目中的 YAML 配置文件（如 base.yaml、strategy.yaml 等）
支持从 .env 文件加载环境变量（如 TUSHARE_TOKEN），用于本地安全调试。
提供 base_config, strategy_config, tushare_token 等变量供各模块直接使用。
"""

import os
from dotenv import load_dotenv
from common.config_loader import load_yaml_config
from common.logger import get_logger
from common.paths import CONFIG_DIR

logger = get_logger("Config")

# === 加载 .env 文件（存放敏感信息） ===
load_dotenv()

# === 要自动加载的 YAML 配置文件名（不含扩展名） ===
CONFIG_FILES = [
    'base',
    'strategy',
    'backtest',
    'trading',
    'model'
]

# === 配置字典容器 ===
configs = {}

# === 加载所有配置文件 ===
for name in CONFIG_FILES:
    try:
        configs[name] = load_yaml_config(os.path.join(CONFIG_DIR, f"{name}.yaml"))
        logger.info(f"[config] ✅ loaded: {name}.yaml")
    except FileNotFoundError:
        configs[name] = {}
        logger.warning(f"[config] ⚠️ missing: {name}.yaml")

# === 快捷访问接口 ===
base_config = configs['base']
strategy_config = configs['strategy']
backtest_config = configs['backtest']
trading_config = configs['trading']
model_config = configs['model']

# === 动态访问函数 ===
def get_config(name: str) -> dict:
    return configs.get(name, {})

# === 读取敏感信息（优先从 .env 获取） ===
tushare_token = os.getenv("TUSHARE_TOKEN") or base_config.get("tushare_token", "")
