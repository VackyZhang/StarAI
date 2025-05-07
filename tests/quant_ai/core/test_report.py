import pandas as pd
from quant_ai.core.report import ReportGenerator

def test_generate_report(tmp_path):
    trades = pd.DataFrame({
        "date": pd.date_range("2023-01-01", periods=3),
        "position": [1, 0, -1],
        "price": [100, 102, 101]
    })
    generator = ReportGenerator()
    report = generator.generate(trades, save_path=tmp_path / "report.csv")
    assert report["returns"].shape[0] == trades.shape[0]
