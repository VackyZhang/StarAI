# tests/quant_ai/core/test_execution.py

import pandas as pd
from quant_ai.core.execution import ExecutionEngine

def test_execute():
    # ✅ 添加 'close' 字段作为 ExecutionEngine 所依赖的价格列
    data = pd.DataFrame({
        "close": [100, 101, 102],
        "volume": [10, 15, 12]
    })
    signals = pd.Series([1, -1, 1])
    engine = ExecutionEngine()
    result = engine.execute(data, signals)

    assert isinstance(result, pd.DataFrame)
    assert "trade" in result.columns
    assert all(result["trade"] == signals * data["close"])
