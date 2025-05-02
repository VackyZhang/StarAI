import os

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 基础路径
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
CONFIG_DIR = os.path.join(PROJECT_ROOT, "config")
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

# 数据目录相关
DATA_RAW_DIR = os.path.join(DATA_DIR, "raw")
DATA_PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
DATA_INTERIM_DIR = os.path.join(DATA_DIR, "interim")

# 配置文件目录
CONFIG_FILES = {
    "base": os.path.join(CONFIG_DIR, "base.yaml"),
    "strategy": os.path.join(CONFIG_DIR, "strategy.yaml"),
    "backtest": os.path.join(CONFIG_DIR, "backtest.yaml"),
    "trading": os.path.join(CONFIG_DIR, "trading.yaml"),
    "model": os.path.join(CONFIG_DIR, "model.yaml"),
}

# 模型存储路径
MODEL_CHECKPOINT_DIR = os.path.join(MODELS_DIR, "checkpoints")

# 确保路径存在（用于初始化）
def ensure_dir(path: str):
    """
    检查路径是否存在，若不存在则创建。
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[paths.py] ✅ 创建目录: {path}")

# 确保所有路径存在
def ensure_all_dirs():
    """
    确保所有重要路径都存在
    """
    ensure_dir(DATA_DIR)
    ensure_dir(CONFIG_DIR)
    ensure_dir(MODELS_DIR)
    ensure_dir(LOG_DIR)
    ensure_dir(DATA_RAW_DIR)
    ensure_dir(DATA_PROCESSED_DIR)
    ensure_dir(DATA_INTERIM_DIR)
    ensure_dir(MODEL_CHECKPOINT_DIR)
