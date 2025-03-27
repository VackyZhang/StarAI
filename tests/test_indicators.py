### 测试 indicators.py

import pandas as pd
from quant_ai.indicators import sma

def test_sma():
    df = pd.DataFrame({"Close": [1, 2, 3, 4, 5]})
    assert sma(df, 2).iloc[-1] == 4.5  # 最后两个数据点的均值