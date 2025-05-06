import pandas as pd
from quant_ai.core.report import ReportGenerator

def test_generate_report():
    trades = pd.DataFrame({
        "trade": [1, -1, 1],
        "price": [100, 102, 105]
    })
    report = ReportGenerator.generate(trades)
    assert isinstance(report, dict)
