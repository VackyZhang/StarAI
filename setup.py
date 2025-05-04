# setup.py
from setuptools import setup, find_packages

setup(
    name="starai",
    version="0.1.0",
    description="AI-driven Quantitative Trading Framework",
    author="Vacky Zhang",
    python_requires=">=3.8",
    package_dir={"": "src"},               # 所有包都在 src/ 下
    packages=find_packages(where="src"),   # 自动发现 src 下的所有子包
    include_package_data=True,
    install_requires=[                     # 如果你想把 requirements.txt 中的依赖也写到这里
        # "pandas>=2.0.0",
        # "numpy>=1.23.0",
        # ...
    ],
)
