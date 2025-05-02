"""
路径模块：管理项目根目录、缓存目录等路径
"""
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
CONFIG_DIR = os.path.join(PROJECT_ROOT, "config")
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")

def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
