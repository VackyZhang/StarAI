"""
配置包：将 common.config_loader 中的接口导出，
方便直接 `import config` 使用。
"""

from common.config_loader import (
    base_config,
    strategy_config,
    backtest_config,
    trading_config,
    model_config,
    get_config,
    load_yaml_config,
    tushare_token,
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
