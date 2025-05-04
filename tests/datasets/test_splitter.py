"""
测试 splitter 拆分功能
"""

import pandas as pd
from datasets.splitter import split_by_ratio


def test_split_by_ratio():
    df = pd.DataFrame({
        "feature1": range(10),
        "feature2": range(10, 20),
        "close": range(100, 110)
    })

    X_train, y_train, X_val, y_val = split_by_ratio(df, split_ratio=(0.6, 0.4))

    assert len(X_train) == 6
    assert len(X_val) == 4
    assert list(X_train.columns) == ["feature1", "feature2"]
