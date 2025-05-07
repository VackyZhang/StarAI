# tests/quant_ai/test_init.py

"""
quant_ai 初始化模块测试：验证主模块是否正确导入各子模块与核心组件。
"""

import quant_ai


def test_import_core_components():
    assert hasattr(quant_ai, "BacktestEngine")
    assert hasattr(quant_ai, "BaseStrategy")
    assert hasattr(quant_ai, "ExecutionEngine")
    assert hasattr(quant_ai, "ReportGenerator")


def test_import_data_modules():
    assert hasattr(quant_ai, "datasource")
    assert hasattr(quant_ai, "loader")
    assert hasattr(quant_ai, "preprocessor")


def test_import_risk_and_trading():
    assert hasattr(quant_ai, "risk_manager")
    assert hasattr(quant_ai, "broker_base")
    assert hasattr(quant_ai, "jqdatasdk")
    assert hasattr(quant_ai, "mock")


def test_import_config():
    assert hasattr(quant_ai, "config")
