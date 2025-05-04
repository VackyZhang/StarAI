"""
测试 preprocessor.py 中的特征预处理函数
"""

import pandas as pd
from data.prepare.preprocessor import normalize_df


def test_normalize_df():
    df = pd.DataFrame({
        "open": [10, 20, 30],
        "volume": [100, 200, 300]
    })

    df_norm = normalize_df(df)

    # 所有数值列应缩放到 [0, 1] 区间
    assert df_norm["open"].min() == 0
    assert df_norm["open"].max() == 1
    assert df_norm["volume"].min() == 0
    assert df_norm["volume"].max() == 1
