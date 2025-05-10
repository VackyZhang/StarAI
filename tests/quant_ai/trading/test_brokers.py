import pytest
import pandas as pd
from quant_ai.trading.mock import MockBroker
from quant_ai.trading.jqdatasdk import JQBroker
import jqdatasdk


def test_mock_broker_execute():
    broker = MockBroker()
    signal = pd.Series([1, -1, 1], index=pd.date_range("2023-01-01", periods=3))
    data = pd.DataFrame({
        "close": [100, 102, 101]
    }, index=signal.index)

    result = broker.execute(signal, data)

    assert isinstance(result, pd.DataFrame)
    assert "trade" in result.columns
    assert result["trade"].tolist() == [100, -102, 101]


def test_jqbroker_execute(monkeypatch):
    # ✅ mock jqdatasdk.auth 防止真实登录
    monkeypatch.setattr(jqdatasdk, "auth", lambda u, p: None)

    broker = JQBroker(username="test", password="test")
    signal = pd.Series([1, 0, -1], index=pd.date_range("2023-01-01", periods=3))
    data = pd.DataFrame({
        "close": [10, 11, 12]
    }, index=signal.index)

    result = broker.execute(signal, data)

    assert isinstance(result, pd.DataFrame)
    assert "trade" in result.columns
    assert result["trade"].tolist() == [10, 0, -12]
