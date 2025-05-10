# tests/quant_ai/risk/test_risk_manager.py

import pandas as pd
from quant_ai.risk import RiskManager


def test_risk_manager_check_all_pass():
    # 累计最大仓位 = 480，阈值调高到允许范围内
    trades = pd.DataFrame({"trade": [100, 120, 150, 110]})
    risk_manager = RiskManager(max_drawdown=0.5, max_position=500)
    result = risk_manager.check(trades)
    assert result is True


def test_risk_manager_check_drawdown_fail():
    # 模拟回撤超过 20% 的场景
    trades = pd.DataFrame({"trade": [100000, 110000, 70000]})
    risk_manager = RiskManager(max_drawdown=0.2, max_position=200000)
    result = risk_manager.check(trades)
    assert result is False


def test_risk_manager_check_position_fail():
    # 模拟最大持仓超过阈值
    trades = pd.DataFrame({"trade": [100, 300, 150]})  # 最大持仓 = 550
    risk_manager = RiskManager(max_drawdown=0.5, max_position=200)
    result = risk_manager.check(trades)
    assert result is False
