"""
Common 初始化模块：自动加载和检查项目的基础配置和目录
"""

from common.paths import ensure_all_dirs
from common.logger import get_logger
from dotenv import load_dotenv

# === 加载 .env 文件（存放敏感信息） ===
load_dotenv()

# === 初始化日志系统 ===
logger = get_logger("StarAI")

# === 确保必要目录存在 ===
logger.info("[common] 确保项目目录存在...")
ensure_all_dirs()

# === 提示成功 ===
logger.info("[common] 初始化完成！")
