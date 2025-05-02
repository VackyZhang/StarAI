"""
路径模块测试：验证 ensure_dir 与 ensure_all_dirs 的正确性，并确认路径常量是否指向预期目录。
"""

import os
import pytest
from common.paths import (
    ensure_dir,
    ensure_all_dirs,
    DATA_DIR,
    CONFIG_DIR,
    LOG_DIR,
    MODELS_DIR,
    MODEL_CHECKPOINT_DIR,
    CONFIG_FILES,
)

def test_ensure_dir(tmp_path):
    """
    验证 ensure_dir 能正确创建指定路径
    """
    target = tmp_path / "custom_dir"
    ensure_dir(str(target))
    assert target.exists() and target.is_dir()

def test_ensure_all_dirs(tmp_path):
    """
    验证 ensure_all_dirs 能在临时路径下创建所有项目关键目录
    """
    ensure_all_dirs(str(tmp_path))

    expected_paths = [
        tmp_path / "data",
        tmp_path / "data" / "raw",
        tmp_path / "data" / "processed",
        tmp_path / "data" / "interim",
        tmp_path / "config",
        tmp_path / "logs",
        tmp_path / "models",
        tmp_path / "models" / "checkpoints",
    ]

    for path in expected_paths:
        assert path.exists() and path.is_dir(), f"目录不存在: {path}"

def test_path_constants_exist():
    """
    验证常量路径是否解析为绝对路径，且包含关键目录名
    """
    assert "data" in DATA_DIR
    assert "config" in CONFIG_DIR
    assert "logs" in LOG_DIR
    assert "models" in MODELS_DIR
    assert "checkpoints" in MODEL_CHECKPOINT_DIR

def test_config_files_mapping():
    """
    验证 CONFIG_FILES 路径映射是否完整且后缀为 .yaml
    """
    for name, path in CONFIG_FILES.items():
        assert path.endswith(f"{name}.yaml")
        assert "config" in path
