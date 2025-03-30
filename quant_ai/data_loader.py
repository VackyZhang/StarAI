### 数据获取模块
### 负责从不同的数据源获取市场数据，并进行数据清洗。

import pandas as pd
import yfinance as yf
import time
import random
from typing import Optional
from quant_ai.utils.logger import setup_logger

# 配置日志
logger = setup_logger(__name__)

def load_stock_data(symbol: str, start: str, end: str, max_retries: int = 5) -> pd.DataFrame:
    """获取股票历史数据
    
    Args:
        symbol: 股票代码
        start: 开始日期
        end: 结束日期
        max_retries: 最大重试次数
        
    Returns:
        pd.DataFrame: 包含股票数据的DataFrame
    """
    logger.info(f"开始获取股票 {symbol} 的数据")
    logger.info(f"时间范围：{start} 到 {end}")
    
    for attempt in range(max_retries):
        try:
            logger.info(f"第 {attempt + 1} 次尝试获取数据...")
            
            # 添加随机延时，避免固定间隔
            if attempt > 0:
                base_wait = (attempt + 1) * 10  # 基础等待时间
                random_wait = random.uniform(0, 5)  # 随机额外等待时间
                wait_time = base_wait + random_wait
                logger.info(f"等待 {wait_time:.1f} 秒后重试...")
                time.sleep(wait_time)
            
            stock = yf.download(symbol, start=start, end=end)
            
            if not stock.empty:
                logger.info(f"数据获取成功：{len(stock)} 条记录")
                logger.info("\n数据信息：")
                logger.info(f"数据列：{', '.join(stock.columns)}")
                logger.info(f"数据类型：\n{stock.dtypes}")
                logger.info("\n数据预览：")
                print(stock.round(2))
                logger.info("\n基本统计信息：")
                print(stock.describe().round(2))
                
                stock['Return'] = stock['Close'].pct_change()
                return stock
            else:
                logger.warning(f"获取到的数据为空")
                raise ValueError(f"未能获取到 {symbol} 的数据")
                
        except Exception as e:
            logger.error(f"尝试 {attempt + 1}/{max_retries} 失败: {str(e)}")
            if attempt < max_retries - 1:
                logger.info("准备下一次尝试...")
            else:
                logger.error(f"在 {max_retries} 次尝试后仍然无法获取数据")
                raise Exception(f"在 {max_retries} 次尝试后仍然无法获取数据: {str(e)}")