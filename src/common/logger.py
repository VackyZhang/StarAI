import logging
import sys

def get_logger(name: str = "StarAI", level=None) -> logging.Logger:
    """
    获取配置好的日志记录器，支持字符串或 logging 常量级别。
    如：level="DEBUG" 或 level=logging.DEBUG
    """
    logger = logging.getLogger(name)

    # 添加 handler（仅一次）
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # 设置日志级别（始终设置）
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)
    elif isinstance(level, int):
        pass  # 已是合法级别
    else:
        level = logging.INFO

    logger.setLevel(level)
    return logger
