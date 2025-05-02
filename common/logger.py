import logging
import sys

def get_logger(name: str = "StarAI", level=None) -> logging.Logger:
    """
    获取配置好的日志记录器
    默认日志级别为 INFO，可以通过 `level` 参数传入自定义日志级别。
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        level = level or "INFO"  # 如果没有传递 level，默认为 INFO
        logger.setLevel(getattr(logging, level.upper(), logging.INFO))  # 动态设置日志级别
    return logger
