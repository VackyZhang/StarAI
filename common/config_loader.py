"""
配置加载模块：读取 YAML 文件为 Python 字典
"""
import os
import yaml

def load_yaml_config(path: str) -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"配置文件不存在: {path}")
    with open(path, "r") as f:
        return yaml.safe_load(f)
