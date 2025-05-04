# config/__init__.py

"""
配置包：统一加载项目根 config/*.yaml 和 .env
所有模块都通过 common.config_loader 打底。
"""

from common.config_loader import (
    base_config,
    strategy_config,
    backtest_config,
    trading_config,
    model_config,
    get_config,
    load_yaml_config,
)
from common.config_loader import (
    # 兼容老代码单独导出的 token
    # 如果不需要单独导出，也可删掉下面一行
    tus hare_token
)

__all__ = [
    "base_config",
    "strategy_config",
    "backtest_config",
    "trading_config",
    "model_config",
    "get_config",
    "load_yaml_config",
    "tushare_token",
]
