# setup.py
# 注册 StarAI 下的模块路径（如 config, datasets, data 等）

from setuptools import setup, find_packages

setup(
    name="starai",
    version="0.1.0",
    description="AI-driven Quantitative Trading Framework",
    author="Vacky Zhang",
    packages=find_packages(),  # 自动发现包含 __init__.py 的目录
    include_package_data=True,
    install_requires=[],       # 可以空，实际依赖在 requirements.txt 中管理
    python_requires=">=3.8",
)
