"""
路径管理模块：统一定义项目目录结构，并提供目录创建方法。
"""

import os

# 项目根目录（默认用于运行时）
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 默认路径定义
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
CONFIG_DIR = os.path.join(PROJECT_ROOT, "config")
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

# 子目录
DATA_RAW_DIR = os.path.join(DATA_DIR, "raw")
DATA_PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
DATA_INTERIM_DIR = os.path.join(DATA_DIR, "interim")
MODEL_CHECKPOINT_DIR = os.path.join(MODELS_DIR, "checkpoints")

# 配置文件路径映射（用于验证、引用）
CONFIG_FILES = {
    "base": os.path.join(CONFIG_DIR, "base.yaml"),
    "strategy": os.path.join(CONFIG_DIR, "strategy.yaml"),
    "backtest": os.path.join(CONFIG_DIR, "backtest.yaml"),
    "trading": os.path.join(CONFIG_DIR, "trading.yaml"),
    "model": os.path.join(CONFIG_DIR, "model.yaml"),
}

def ensure_dir(path: str):
    """
    创建单个目录（如果不存在）
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[paths] ✅ 创建目录: {path}")

def ensure_all_dirs(base_path: str = PROJECT_ROOT):
    """
    确保项目所有关键目录存在
    支持传入自定义 base_path（默认使用项目根目录）
    """
    paths = [
        os.path.join(base_path, "data"),
        os.path.join(base_path, "data", "raw"),
        os.path.join(base_path, "data", "processed"),
        os.path.join(base_path, "data", "interim"),
        os.path.join(base_path, "config"),
        os.path.join(base_path, "logs"),
        os.path.join(base_path, "models"),
        os.path.join(base_path, "models", "checkpoints"),
    ]
    for p in paths:
        ensure_dir(p)
