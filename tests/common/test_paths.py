import os
import pytest
from common.paths import ensure_dir, DATA_DIR, CONFIG_DIR, ensure_all_dirs

def test_ensure_dir(tmp_path):
    test_dir = tmp_path / "test_dir"
    ensure_dir(str(test_dir))
    assert test_dir.exists()

def test_ensure_all_dirs(tmp_path):
    ensure_all_dirs()  # 使用临时路径
    assert (tmp_path / "data").exists()
    assert (tmp_path / "config").exists()

def test_paths():
    assert DATA_DIR == os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "data")
    assert CONFIG_DIR == os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "config")
