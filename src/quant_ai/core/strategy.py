# quant_ai/core/strategy.py

"""
策略模块：定义策略接口和基础示例实现。
"""

import pandas as pd
from common.logger import get_logger

logger = get_logger("Strategy")

class BaseStrategy:
    def __init__(self):
        pass

    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        logger.info("⚙️ 生成固定信号（买入=1）")
        return pd.Series(1, index=data.index)  # 示例策略：全买入
