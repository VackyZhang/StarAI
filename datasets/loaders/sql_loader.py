"""
MySQL 数据加载模块：从 MySQL 数据库加载数据集
"""
import mysql.connector  # 使用 mysql 连接器
import pandas as pd
import os
from datasets.configs.dataset_config import DATASET_CONFIG
from common.logger import get_logger

logger = get_logger("MySqlLoader")

def load_dataset(name: str, split: str = "train", index_col: str = "date") -> pd.DataFrame:
    """
    从 MySQL 数据库加载数据集

    参数:
        name (str): 数据集名称，如 "000001.SZ"
        split (str): 数据集切分，如 "train", "test"
        index_col (str): 设置 DataFrame 的索引列，默认为 "date"

    返回:
        pd.DataFrame: 返回加载的数据集
    """
    db_config = DATASET_CONFIG["mysql_config"]  # 假设 mysql 配置存储在 dataset_config.yaml 中

    # 从配置文件中读取 MySQL 连接参数
    host = db_config["host"]
    user = db_config["user"]
    password = db_config["password"]
    database = db_config["database"]

    # 连接 MySQL 数据库
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    except mysql.connector.Error as err:
        logger.error(f"❌ MySQL 连接失败: {err}")
        raise

    # 查询语句
    query = f"SELECT * FROM {name}_{split}"

    try:
        df = pd.read_sql(query, conn)
    except Exception as e:
        logger.error(f"❌ 查询失败: {e}")
        raise

    finally:
        conn.close()

    # 设置索引列
    df.set_index(index_col, inplace=True)

    return df
