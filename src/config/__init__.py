# src/config/__init__.py
"""
配置包：统一通过 common.config_loader 加载所有 YAML + .env 配置
"""

from common.config_loader import (
    base_config,
    strategy_config,
    backtest_config,
    trading_config,
    model_config,
    get_config,
)

# 为兼容老代码，额外导出 tushare_token
tushare_token = base_config.get("tushare_token", "")

__all__ = [
    "base_config",
    "strategy_config",
    "backtest_config",
    "trading_config",
    "model_config",
    "get_config",
    "tushare_token",
]
