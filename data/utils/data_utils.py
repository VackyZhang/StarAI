# 数据工具函数，如文件检查、路径创建等
import os

def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
