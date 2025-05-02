"""
测试 config/__init__.py 中的配置加载逻辑、环境变量加载、get_config 访问能力。
"""

import os
import pytest
from dotenv import load_dotenv
from config import (
    base_config,
    strategy_config,
    backtest_config,
    trading_config,
    model_config,
    get_config,
    tushare_token
)

def test_base_config_fields():
    assert "data_dir" in base_config
    assert "log_dir" in base_config
    assert "project_name" in base_config

def test_strategy_config_fields():
    assert "strategy_name" in strategy_config
    assert "parameters" in strategy_config
    assert "risk_parameters" in strategy_config

def test_model_config_structure():
    assert isinstance(model_config, dict)

def test_get_config():
    assert get_config("base") == base_config
    assert get_config("non_existing") == {}  # 缺失文件也不会报错

def test_tushare_token_loaded():
    load_dotenv()
    token_from_env = os.getenv("TUSHARE_TOKEN")
    assert tushare_token == token_from_env or tushare_token == base_config.get("tushare_token", "")
