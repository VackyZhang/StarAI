"""
性能监控模块测试：验证 timeit 和 monitor_resource_usage 装饰器运行正常，无异常输出或警告。
"""

from common.monitor import timeit, monitor_resource_usage

@timeit
def sample_add(a, b):
    return a + b

@monitor_resource_usage
def simulate_workload():
    total = 0
    for i in range(10000):
        total += i
    return total

def test_timeit_decorator():
    """
    验证 timeit 装饰器是否能包裹正常函数
    """
    result = sample_add(2, 3)
    assert result == 5

def test_monitor_resource_usage_decorator():
    """
    验证资源监控装饰器是否能正常执行
    """
    result = simulate_workload()
    assert result > 0
