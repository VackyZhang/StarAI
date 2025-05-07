import pandas as pd
from quant_ai.core.execution import ExecutionEngine

def test_execute():
    data = pd.DataFrame({
        "price": [100, 101, 102],
        "volume": [10, 15, 12]
    })
    signals = pd.Series([1, -1, 1])
    engine = ExecutionEngine()
    result = engine.execute(data, signals)
    assert isinstance(result, pd.DataFrame)
    assert "position" in result.columns
