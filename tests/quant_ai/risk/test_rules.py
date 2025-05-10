# tests/quant_ai/risk/test_rules.py

import pandas as pd
from quant_ai.risk.rules import MaxPositionRule


def test_max_position_rule_applies_correctly():
    # 模拟市场数据
    data = pd.DataFrame({"price": [100, 101, 102, 103, 104]})
    signals = pd.Series([1, 1, 1, 0, 1])  # 多次买入尝试

    rule = MaxPositionRule(max_position=2)
    filtered = rule.apply(data, signals)

    # 应该只有前两次买入生效，其它买入应被取消
    expected = pd.Series([1, 1, 0, 0, 0])
    pd.testing.assert_series_equal(filtered, expected)
