"""
路径管理模块：统一定义项目目录结构，并提供目录创建方法。
"""

from pathlib import Path

# 项目根目录：从 src/common/paths.py 向上追溯三层
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# 数据目录
DATA_DIR       = PROJECT_ROOT / "data"
DATA_RAW_DIR   = DATA_DIR / "raw"
DATA_INTERIM_DIR   = DATA_DIR / "interim"
DATA_PROCESSED_DIR = DATA_DIR / "processed"
DATA_EXTERNAL_DIR  = DATA_DIR / "external"
DATA_METADATA_DIR  = DATA_DIR / "metadata"

# 模型目录
MODELS_DIR            = PROJECT_ROOT / "models"
MODEL_CHECKPOINT_DIR  = MODELS_DIR / "checkpoints"
MODEL_FINAL_DIR       = MODELS_DIR / "final"
MODEL_LOGS_DIR        = MODELS_DIR / "logs"

# 日志目录
LOGS_DIR    = PROJECT_ROOT / "logs"

# 配置目录
CONFIG_DIR  = PROJECT_ROOT / "config"
CONFIG_FILES = {
    name: CONFIG_DIR / f"{name}.yaml"
    for name in ("base", "strategy", "backtest", "trading", "model", "optimizer", "risk")
}

# 测试输出目录（如果需要单独存放测试生成内容）
TEST_OUTPUT_DIR = PROJECT_ROOT / "tests" / "output"

def ensure_dir(path: Path):
    """
    创建单个目录（如果不存在）
    """
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        print(f"[paths] ✅ 创建目录: {path}")

def ensure_all_dirs(base_path: Path = PROJECT_ROOT):
    """
    确保项目所有关键目录存在
    支持传入自定义 base_path（默认使用项目根目录）
    """
    dirs = [
        DATA_RAW_DIR,
        DATA_INTERIM_DIR,
        DATA_PROCESSED_DIR,
        DATA_EXTERNAL_DIR,
        DATA_METADATA_DIR,
        MODELS_DIR,
        MODEL_CHECKPOINT_DIR,
        MODEL_FINAL_DIR,
        MODEL_LOGS_DIR,
        LOGS_DIR,
        CONFIG_DIR,
        TEST_OUTPUT_DIR,
    ]
    for d in dirs:
        ensure_dir(d)
