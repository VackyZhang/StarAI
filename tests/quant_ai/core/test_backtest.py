"""
回测引擎单元测试
"""

import pandas as pd
from quant_ai.core.backtest import BacktestEngine


def test_backtest_run(monkeypatch):
    # 模拟策略（批量生成信号）
    class DummyStrategy:
        def generate_signals(self, data: pd.DataFrame):
            return pd.Series([1] * len(data), index=data.index)

    # 模拟执行引擎
    class DummyExecutionEngine:
        def execute(self, data: pd.DataFrame, signals: pd.Series):
            trades = data.copy()
            trades["signal"] = signals
            trades["trade"] = trades["signal"] * trades["price"]
            return trades

    # 模拟报告生成器
    class DummyReportGenerator:
        def generate(self, trades: pd.DataFrame):
            assert isinstance(trades, pd.DataFrame), "生成的交易数据应为 DataFrame"
            assert "trade" in trades.columns, "交易结果中应包含 'trade' 列"
            assert len(trades) > 0, "交易记录不应为空"

    # 创建回测引擎并注入 mock 组件
    engine = BacktestEngine()
    engine.strategy = DummyStrategy()
    engine.execution = DummyExecutionEngine()
    engine.report = DummyReportGenerator()

    # 构造模拟数据，增加日期索引
    engine.data = pd.DataFrame({
        "price": [100, 102, 105],
        "volume": [10, 15, 12]
    }, index=pd.date_range("2023-01-01", periods=3))

    # 执行回测
    engine.run_backtest()
