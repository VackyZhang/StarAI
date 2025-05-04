# config/__init__.py

"""
配置包：将 common.config_loader 中的接口导出，
方便在 examples/ 或其它地方直接 `import config`。
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

__all__ = [
    "base_config",
    "strategy_config",
    "backtest_config",
    "trading_config",
    "model_config",
    "get_config",
    "load_yaml_config",
]
