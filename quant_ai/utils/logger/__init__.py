### 日志管理模块
### 负责配置和管理整个项目的日志输出

from .formatter import ColoredFormatter
from .setup import setup_logger

__all__ = ['ColoredFormatter', 'setup_logger'] 