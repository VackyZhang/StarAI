import pandas as pd
from quant_ai.core.execution import ExecutionEngine

def test_execute_orders():
    engine = ExecutionEngine()
    signals = pd.Series([1, -1, 1])
    price_data = pd.DataFrame({"price": [100, 101, 102]})
    trades = [engine.execute(signal, row) for signal, row in zip(signals, price_data.itertuples(index=False))]
    assert trades is not None
    assert len(trades) == 3
