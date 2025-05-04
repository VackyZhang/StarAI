import yaml
import os

# 配置文件路径
config_path = os.path.join(os.path.dirname(__file__), 'dataset_config.yaml')

# 加载 YAML 配置文件
with open(config_path, 'r') as f:
    DATASET_CONFIG = yaml.safe_load(f)

# 导出配置
__all__ = ["DATASET_CONFIG"]
