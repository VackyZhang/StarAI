# tests/quant_ai/risk/test_metrics.py

import pandas as pd
from quant_ai.risk import metrics


def test_compute_cumulative_returns():
    trades = pd.DataFrame({
        "date": pd.date_range("2023-01-01", periods=5),
        "trade": [1, -0.5, 1.5, -2, 1]
    }).set_index("date")

    result = metrics.compute_cumulative_returns(trades)
    expected = pd.Series([1, 0.5, 2.0, 0.0, 1.0], index=trades.index, name="cumulative")
    pd.testing.assert_series_equal(result, expected)


def test_compute_max_drawdown():
    series = pd.Series([1, 2, 1.5, 3, 2])
    max_dd = metrics.compute_max_drawdown(series)
    assert isinstance(max_dd, float)
    assert round(max_dd, 2) == 1.0


def test_compute_sharpe_ratio_normal():
    returns = pd.Series([0.01, 0.02, -0.01, 0.03])
    sharpe = metrics.compute_sharpe_ratio(returns)
    assert isinstance(sharpe, float)
    assert sharpe != 0.0


def test_compute_sharpe_ratio_zero_std():
    returns = pd.Series([0.01, 0.01, 0.01])
    sharpe = metrics.compute_sharpe_ratio(returns)
    assert sharpe == 0.0


def test_compute_daily_returns():
    trades = pd.DataFrame({
        "date": pd.date_range("2023-01-01", periods=3),
        "trade": [100, 110, 105]
    }).set_index("date")
    result = metrics.compute_daily_returns(trades)
    pd.testing.assert_series_equal(result, trades["trade"])
