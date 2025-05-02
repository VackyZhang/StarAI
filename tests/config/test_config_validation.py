# tests/config/test_config_validation.py
# 用于验证 config/*.yaml 是否能正确加载并包含必要字段

import os
import pytest
from config import (
    base_config, strategy_config, backtest_config,
    trading_config, model_config, get_config, tushare_token
)

def test_base_config():
    assert 'data_dir' in base_config
    assert 'log_dir' in base_config
    assert 'timezone' in base_config

def test_strategy_config():
    assert strategy_config['strategy_name']
    assert isinstance(strategy_config['parameters'], dict)

def test_backtest_config():
    assert backtest_config['initial_cash'] > 0
    assert 'start_date' in backtest_config
    assert 'end_date' in backtest_config

def test_trading_config():
    assert isinstance(trading_config['auto_trade'], bool)

def test_model_config():
    assert model_config['model_type'] in ['xgboost', 'lightgbm']

def test_env_token_loaded():
    assert tushare_token is not None
