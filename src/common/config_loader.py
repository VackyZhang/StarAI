"""
配置加载模块：读取项目根 config/*.yaml 和 .env，然后标准化关键字段。
同时，提供一个独立的 load_yaml_config 工具函数。
"""

import os
from pathlib import Path
import yaml

from common.paths import PROJECT_ROOT

# 指向项目根下的 config 目录
_CONFIG_DIR = PROJECT_ROOT / "config"


class ConfigLoader:
    def __init__(self, env_file: Path = None):
        # 加载 .env（如果存在）
        if env_file and env_file.exists():
            from dotenv import load_dotenv
            load_dotenv(str(env_file))

        self.configs = {}
        self._load_all()

    def _load_yaml(self, path: Path) -> dict:
        if not path.exists():
            raise FileNotFoundError(f"缺失配置文件: {path}")
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    def _load_all(self):
        # 加载 base, strategy, backtest, trading, model
        for name in ("base", "strategy", "backtest", "trading", "model"):
            self.configs[name] = self._load_yaml(_CONFIG_DIR / f"{name}.yaml")

        base = self.configs["base"]

        # 解析 data_dir
        data_dir = Path(base.get("data_dir", PROJECT_ROOT / "data"))
        base["data_dir"] = (PROJECT_ROOT / data_dir) if not data_dir.is_absolute() else data_dir

        # 解析 processed_dir
        processed = Path(base.get("processed_dir", PROJECT_ROOT / "data" / "processed"))
        base["processed_dir"] = (PROJECT_ROOT / processed) if not processed.is_absolute() else processed

        # 解析 log_dir
        log_dir = Path(base.get("log_dir", PROJECT_ROOT / "logs"))
        base["log_dir"] = (PROJECT_ROOT / log_dir) if not log_dir.is_absolute() else log_dir

        # 时区
        base["timezone"] = base.get("timezone", "UTC")

        # .env 覆盖 tushare_token
        token = os.getenv("TUSHARE_TOKEN")
        if token:
            base["tushare_token"] = token

    def get(self, name: str) -> dict:
        return self.configs.get(name, {})


# 单例化
_loader = ConfigLoader(env_file=PROJECT_ROOT / ".env")
base_config     = _loader.get("base")
strategy_config = _loader.get("strategy")
backtest_config = _loader.get("backtest")
trading_config  = _loader.get("trading")
model_config    = _loader.get("model")


def get_config(name: str) -> dict:
    """
    动态获取某一配置字典，name 应为：base、strategy、backtest、trading 或 model
    """
    return _loader.get(name)


def load_yaml_config(path: str) -> dict:
    """
    独立的 YAML 加载工具。
    如果文件不存在，抛出 FileNotFoundError。
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"配置文件不存在: {path}")
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
