import pandas as pd
from quant_ai.core.strategy import BaseStrategy

class DummyStrategy(BaseStrategy):
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        data["signal"] = 1
        return data

def test_generate_signals():
    data = pd.DataFrame({"price": [10, 11, 12]})
    strategy = DummyStrategy({})
    result = strategy.generate_signals(data)
    assert "signal" in result.columns
    assert result["signal"].iloc[0] == 1
