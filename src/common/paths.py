"""
路径管理模块：统一定义项目目录结构，并提供目录创建方法。
"""

from pathlib import Path

# === 私有：项目根目录 Path ===
_PROJECT_ROOT = Path(__file__).resolve().parents[2]

# === 对外导出：项目根目录 Path ===
PROJECT_ROOT = _PROJECT_ROOT

# === 相对目录列表（仅用于 ensure_all_dirs） ===
_REL_DIRS = [
    Path("data"),
    Path("data") / "raw",
    Path("data") / "processed",
    Path("data") / "interim",
    Path("config"),
    Path("logs"),
    Path("models"),
    Path("models") / "checkpoints",
]

# =============== 公共常量 (str 类型) ===============
DATA_DIR             = str(_PROJECT_ROOT / "data")
DATA_RAW_DIR         = str(_PROJECT_ROOT / "data" / "raw")
DATA_INTERIM_DIR     = str(_PROJECT_ROOT / "data" / "interim")
DATA_PROCESSED_DIR   = str(_PROJECT_ROOT / "data" / "processed")

MODELS_DIR           = str(_PROJECT_ROOT / "models")
MODEL_CHECKPOINT_DIR = str(_PROJECT_ROOT / "models" / "checkpoints")

LOG_DIR              = str(_PROJECT_ROOT / "logs")
LOGS_DIR             = LOG_DIR  # 兼容

CONFIG_DIR           = str(_PROJECT_ROOT / "src" / "config")

# 只映射五个核心配置文件
CONFIG_FILES = {
    name: str(Path(CONFIG_DIR) / f"{name}.yaml")
    for name in ("base", "strategy", "backtest", "trading", "model")
}


def ensure_dir(path):
    """
    创建单个目录（如果不存在）。
    支持传入 str 或 pathlib.Path。
    """
    p = Path(path)
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)
        print(f"[paths] ✅ 创建目录: {p}")


def ensure_all_dirs(base_path=PROJECT_ROOT):
    """
    确保项目所有关键目录存在。
    支持传入自定义 base_path （str 或 Path），默认使用项目根目录。
    仅创建以下目录：
      data, data/raw, data/processed, data/interim,
      config, logs, models, models/checkpoints
    """
    base = Path(base_path)
    for rel in _REL_DIRS:
        ensure_dir(base / rel)
