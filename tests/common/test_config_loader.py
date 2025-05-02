"""
配置加载测试模块：验证 config 下各 YAML 配置文件结构、get_config 动态加载函数、.env 文件是否成功加载。
"""

import os
import pytest
from dotenv import load_dotenv
from common.paths import CONFIG_FILES, CONFIG_DIR
from common.config_loader import load_yaml_config
from config import (
    base_config,
    strategy_config,
    backtest_config,
    trading_config,
    model_config,
    get_config,  # ✅ 确保已导入
)

def test_load_dotenv():
    """
    验证 .env 文件是否正确加载 TUSHARE_TOKEN（只校验存在性）
    """
    load_dotenv()
    token = os.getenv("TUSHARE_TOKEN")
    assert token is not None and token != "", f"TUSHARE_TOKEN = {token}"

def test_base_config():
    assert "data_dir" in base_config
    assert "processed_dir" in base_config
    assert "log_dir" in base_config
    assert "project_name" in base_config

def test_strategy_config():
    assert "strategy_name" in strategy_config
    assert "parameters" in strategy_config
    assert "risk_parameters" in strategy_config

def test_backtest_config():
    assert isinstance(backtest_config, dict)

def test_trading_config():
    assert isinstance(trading_config, dict)

def test_model_config():
    assert isinstance(model_config, dict)

def test_get_config():
    assert get_config("base") == base_config
    assert get_config("strategy") == strategy_config
    assert get_config("backtest") == backtest_config
    assert get_config("trading") == trading_config
    assert get_config("model") == model_config
    assert get_config("non_existing") == {}

def test_invalid_config_file():
    with pytest.raises(FileNotFoundError):
        load_yaml_config(os.path.join(CONFIG_DIR, "non_existing.yaml"))

def test_config_paths():
    for name, path in CONFIG_FILES.items():
        assert name in ["base", "strategy", "backtest", "trading", "model"]
        assert path.endswith(f"{name}.yaml")
        assert os.path.basename(path) == f"{name}.yaml"
