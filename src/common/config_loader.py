"""
配置加载模块：读取 src/config/*.yaml 和 .env，然后标准化常用字段。
"""

import os
from pathlib import Path
import yaml

from common.paths import PROJECT_ROOT, CONFIG_DIR

class ConfigLoader:
    """
    将 src/config 下的 YAML 文件加载到字典，
    并把 data_dir, processed_dir, log_dir, timezone 等字段解析成绝对路径或标准值。
    """

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
        # 要加载的配置列表
        for name in ("base", "strategy", "backtest", "trading", "model"):
            cfg = self._load_yaml(CONFIG_DIR / f"{name}.yaml")
            self.configs[name] = cfg

        # ===== 处理 base.yaml 中的常用字段 =====
        base = self.configs["base"]

        # data_dir
        data_dir = Path(base.get("data_dir", PROJECT_ROOT / "data"))
        if not data_dir.is_absolute():
            data_dir = PROJECT_ROOT / data_dir
        base["data_dir"] = data_dir

        # processed_dir
        processed = Path(base.get("processed_dir", PROJECT_ROOT / "data" / "processed"))
        if not processed.is_absolute():
            processed = PROJECT_ROOT / processed
        base["processed_dir"] = processed

        # log_dir
        log_dir = Path(base.get("log_dir", PROJECT_ROOT / "logs"))
        if not log_dir.is_absolute():
            log_dir = PROJECT_ROOT / log_dir
        base["log_dir"] = log_dir

        # 时区
        base["timezone"] = base.get("timezone", "UTC")

        # .env 中的 TUSHARE_TOKEN 覆盖
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
    return _loader.get(name)
