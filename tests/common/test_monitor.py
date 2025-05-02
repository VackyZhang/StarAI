import time
import pytest
from common.monitor import timeit
from common.logger import get_logger

logger = get_logger("TestMonitor")

# 测试函数耗时监控
@timeit
def test_func():
    time.sleep(0.1)
    return "done"

def test_timeit_decorator(caplog):
    test_func()

    # 验证是否打印了耗时日志
    assert "耗时" in caplog.text

# 测试资源监控
from common.monitor import monitor_resource_usage

@monitor_resource_usage
def test_func_with_resources():
    time.sleep(0.1)
    return "done"

def test_resource_usage_monitoring(caplog):
    test_func_with_resources()

    assert "CPU 使用" in caplog.text
    assert "内存使用" in caplog.text
