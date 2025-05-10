# tests/quant_ai/data/test_preprocessor.py

import pandas as pd
import numpy as np
from quant_ai.data.preprocessor import DataPreprocessor


def test_transform_with_ffill_and_normalization():
    df = pd.DataFrame({
        "price": [100, None, 102],
        "volume": [10, 12, None]
    })

    processor = DataPreprocessor(method="ffill", normalize=True)
    result = processor.transform(df)

    # 检查是否填充缺失值
    assert not result.isnull().any().any(), "仍存在缺失值"

    # 检查是否标准化（均值约等于0，标准差约等于1）
    np.testing.assert_allclose(result.mean().values, [0.0, 0.0], atol=1e-6)
    np.testing.assert_allclose(result.std(ddof=0).values, [1.0, 1.0], atol=1e-6)


def test_transform_with_zero_fill_and_no_normalization():
    df = pd.DataFrame({
        "a": [1, None, 3],
        "b": [None, 2, 4]
    })

    # 使用 zero 填充 + 不归一化
    processor = DataPreprocessor(method="zero", normalize=False)
    result = processor.transform(df)

    assert (result.iloc[1, 0] == 0)
    assert (result.iloc[0, 1] == 0)
    assert not result.isnull().any().any()


def test_transform_with_empty_dataframe():
    processor = DataPreprocessor()
    empty_df = pd.DataFrame()

    result = processor.transform(empty_df)
    assert result.empty
