"""
测试 features 特征构造模块
"""

import pandas as pd
from datasets.features import add_technical_features


def test_add_technical_features():
    df = pd.DataFrame({
        "close": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    })

    df_feat = add_technical_features(df)

    assert "MA_5" in df_feat.columns
    assert "MA_10" in df_feat.columns
    assert not df_feat.isnull().any().any()
