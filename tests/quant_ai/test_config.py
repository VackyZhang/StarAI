# tests/quant_ai/test_config.py

import pytest
from quant_ai.config import get_config, base_config, strategy_config, backtest_config, trading_config, model_config, risk_config

def test_get_config():
    """测试 get_config 函数"""
    assert get_config("base") == base_config
    assert get_config("strategy") == strategy_config
    assert get_config("backtest") == backtest_config
    assert get_config("trading") == trading_config
    assert get_config("model") == model_config
    assert get_config("risk") == risk_config

def test_missing_config():
    """测试无效配置名称"""
    assert get_config("non_existing") == {}

def test_base_config():
    """验证 base_config 配置内容"""
    assert "data_dir" in base_config
    assert "processed_dir" in base_config
    assert "log_dir" in base_config
    assert "project_name" in base_config

def test_strategy_config():
    """验证 strategy_config 配置内容"""
    assert "strategy_name" in strategy_config
    assert "parameters" in strategy_config
    assert "risk_parameters" in strategy_config

def test_backtest_config():
    """验证 backtest_config 配置内容"""
    assert isinstance(backtest_config, dict)

def test_trading_config():
    """验证 trading_config 配置内容"""
    assert isinstance(trading_config, dict)

def test_model_config():
    """验证 model_config 配置内容"""
    assert isinstance(model_config, dict)

def test_risk_config():
    """验证 risk_config 配置内容"""
    assert isinstance(risk_config, dict)
