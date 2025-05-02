import time
import psutil
from functools import wraps
from common.logger import get_logger

logger = get_logger("Monitor")

def timeit(func):
    """
    函数执行时间监控装饰器
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f"⏱️ {func.__name__} 耗时: {elapsed:.3f}s")
        return result
    return wrapper

def monitor_resource_usage(func):
    """
    资源使用监控装饰器（CPU、内存）
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 获取当前的 CPU 和内存使用情况
        cpu_before = psutil.cpu_percent(interval=0.1)
        memory_before = psutil.virtual_memory().percent

        # 执行函数
        result = func(*args, **kwargs)

        # 获取执行后的资源使用情况
        cpu_after = psutil.cpu_percent(interval=0.1)
        memory_after = psutil.virtual_memory().percent

        logger.info(f"💻 {func.__name__} CPU 使用: {cpu_after - cpu_before}%")
        logger.info(f"💻 {func.__name__} 内存使用: {memory_after - memory_before}%")
        return result

    return wrapper
