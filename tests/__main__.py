"""
一键运行 tests/ 下所有测试模块，用于调试或命令行执行
等价于运行：pytest tests/
"""

import pytest
import sys

if __name__ == "__main__":
    sys.exit(pytest.main(["-v", "tests/"]))
