import pandas as pd
from quant_ai.core.strategy import BaseStrategy

def test_generate_signal():
    strategy = BaseStrategy()
    row = {"price": 100}
    signal = strategy.generate_signal(row)
    assert signal in [-1, 0, 1]
