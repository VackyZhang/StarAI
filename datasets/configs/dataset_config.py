"""
读取 dataset_config.yaml 并暴露为 DATASET_CONFIG 全局变量
"""
import yaml
import os

config_path = os.path.join(os.path.dirname(__file__), 'dataset_config.yaml')
with open(config_path, 'r') as f:
    DATASET_CONFIG = yaml.safe_load(f)
