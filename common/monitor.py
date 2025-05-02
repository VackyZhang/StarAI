"""
性能监控模块：提供耗时统计装饰器等工具
"""
import time
from functools import wraps
from common.logger import get_logger

logger = get_logger("Monitor")

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f"⏱️ {func.__name__} 耗时: {elapsed:.3f}s")
        return result
    return wrapper
