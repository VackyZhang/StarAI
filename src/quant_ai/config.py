import os
import yaml

CONFIG_ROOT = os.path.join(os.path.dirname(__file__), '..', 'config')

def load_config(name: str) -> dict:
    file_path = os.path.join(CONFIG_ROOT, f'{name}.yaml')
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# 快捷访问
base_config = load_config('base')
strategy_config = load_config('strategy')
backtest_config = load_config('backtest')
trading_config = load_config('trading')
