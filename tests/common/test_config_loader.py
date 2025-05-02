import os
import pytest
from common.paths import CONFIG_FILES
from config import base_config, strategy_config, backtest_config, trading_config, model_config
from dotenv import load_dotenv

def test_load_dotenv():
    """
    验证 .env 文件是否正确加载 TUSHARE_TOKEN
    """
    load_dotenv()  # 确保 .env 被加载
    tushare_token = os.getenv("TUSHARE_TOKEN")
    assert tushare_token == "your_actual_token_here", f"TUSHARE_TOKEN = {tushare_token}"

def test_base_config():
    """
    验证 base.yaml 配置文件是否加载成功，并且关键字段存在
    """
    assert "data_dir" in base_config
    assert "processed_dir" in base_config

def test_strategy_config():
    """
    验证 strategy.yaml 配置文件是否加载成功，并且字段完整
    """
    assert "strategy_name" in strategy_config
    assert "risk_parameters" in strategy_config

def test_get_config():
    """
    验证动态获取配置的功能
    """
    assert get_config("base") == base_config
    assert get_config("strategy") == strategy_config
    assert get_config("backtest") == backtest_config
    assert get_config("trading") == trading_config
    assert get_config("model") == model_config

def test_invalid_config_file():
    """
    验证配置文件不存在时的处理
    """
    with pytest.raises(FileNotFoundError):
        load_yaml_config(os.path.join(CONFIG_DIR, 'non_existing.yaml'))

def test_config_paths():
    """
    验证配置路径是否正确
    """
    assert CONFIG_FILES["base"] == "config/base.yaml"
