# quant_ai/risk/risk_manager.py

"""
风控管理模块：负责管理并应用各类风控规则。
"""

from typing import List, Optional
import pandas as pd
from common.logger import get_logger
from quant_ai.risk.rules import RiskRule, MaxPositionRule
from quant_ai.risk.metrics import compute_cumulative_returns, compute_max_drawdown

logger = get_logger("RiskManager")


class RiskManager:
    """
    风控管理器：对策略信号应用所有注册的风控规则，并支持回测后风控检查。
    """

    def __init__(
        self,
        rules: Optional[List[RiskRule]] = None,
        max_position: Optional[int] = None,
        max_drawdown: Optional[float] = None
    ):
        """
        初始化风控管理器。

        参数:
            rules (List[RiskRule], optional): 自定义风控规则列表
            max_position (int, optional): 最大持仓数，若指定将添加对应规则
            max_drawdown (float, optional): 最大允许回撤（0.1 表示 10%）
        """
        self.rules = rules or []

        if max_position is not None:
            self.register_rule(MaxPositionRule(max_position))

        self.max_drawdown = max_drawdown  # 注意：最大回撤规则适用于回测后检查

    def register_rule(self, rule: RiskRule) -> None:
        """
        注册一个新的风控规则。

        参数:
            rule (RiskRule): 实现了 apply 接口的风控规则对象
        """
        logger.info(f"📋 注册风控规则: {rule.__class__.__name__}")
        self.rules.append(rule)

    def apply_rules(self, data: pd.DataFrame, signals: pd.Series) -> pd.Series:
        """
        依次对信号应用所有风控规则。

        参数:
            data (pd.DataFrame): 市场数据
            signals (pd.Series): 原始策略信号

        返回:
            pd.Series: 应用风控规则后的信号
        """
        logger.info(f"🔒 应用风控规则，总数={len(self.rules)}")
        filtered = signals.copy()
        for rule in self.rules:
            filtered = rule.apply(data, filtered)
        return filtered

    def check_after_backtest(self, trades: pd.DataFrame) -> bool:
        """
        回测后执行的风控检查（如最大回撤、最大持仓限制）。

        参数:
            trades (pd.DataFrame): 包含 'trade' 列的交易记录

        返回:
            bool: 是否通过风控（True = 合格）
        """
        passed = True

        if self.max_drawdown is not None:
            cumulative_returns = compute_cumulative_returns(trades)
            max_dd = compute_max_drawdown(cumulative_returns)
            logger.info(f"📉 回测最大回撤: {max_dd:.2%}，允许上限: {self.max_drawdown:.2%}")
            if max_dd > self.max_drawdown:
                logger.warning("❌ 违反最大回撤限制")
                passed = False

        for rule in self.rules:
            if isinstance(rule, MaxPositionRule):
                max_position = trades["trade"].cumsum().max()
                logger.info(f"📊 最大持仓值: {max_position}，限制值: {rule.max_position}")
                if max_position > rule.max_position:
                    logger.warning("❌ 超过最大持仓限制")
                    passed = False

        if passed:
            logger.info("✅ 风控检查通过")

        return passed

    def check(self, trades: pd.DataFrame) -> bool:
        """
        通用风控检查入口，向下兼容测试调用。

        参数:
            trades (pd.DataFrame): 包含 'trade' 列的交易记录

        返回:
            bool: 风控是否通过
        """
        return self.check_after_backtest(trades)
