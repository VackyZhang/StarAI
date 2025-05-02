import os
import yaml

def load_yaml_config(path: str) -> dict:
    """
    加载指定路径的 YAML 配置文件并返回字典。
    如果文件不存在，抛出 FileNotFoundError。
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"配置文件不存在: {path}")
    with open(path, "r") as f:
        return yaml.safe_load(f)
