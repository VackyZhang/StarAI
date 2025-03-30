### 日志设置
### 负责配置和初始化日志记录器

import logging
import sys
from .formatter import ColoredFormatter

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """设置并返回一个配置好的日志记录器
    
    Args:
        name: 日志记录器名称
        level: 日志级别，默认为 INFO
        
    Returns:
        logging.Logger: 配置好的日志记录器
    """
    # 清除所有已存在的处理器
    logger = logging.getLogger(name)
    logger.handlers = []
    
    # 设置日志级别
    logger.setLevel(level)
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(ColoredFormatter())
    logger.addHandler(console_handler)
    
    # 防止日志向上传播
    logger.propagate = False
    
    return logger 