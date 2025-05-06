# tests/quant_ai/test_init.py

import pytest
import quant_ai

def test_quant_ai_import():
    """测试 quant_ai 模块的导入是否成功"""
    assert hasattr(quant_ai, "backtest")
    assert hasattr(quant_ai, "execution")
    assert hasattr(quant_ai, "report")
    assert hasattr(quant_ai, "strategy")
    assert hasattr(quant_ai, "datasource")
    assert hasattr(quant_ai, "loader")
    assert hasattr(quant_ai, "preprocessor")
    assert hasattr(quant_ai, "risk_manager")
    assert hasattr(quant_ai, "broker_base")
    assert hasattr(quant_ai, "jqdatasdk")
    assert hasattr(quant_ai, "mock")
