# setup.py

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="starai",
    version="0.1.0",
    description="AI-driven Quantitative Trading Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vacky Zhang",
    python_requires=">=3.8",
    # 告诉 setuptools：大部分包都在 src/ 下，但有个 config 包在项目根 config/
    package_dir={
        "": "src",
        "config": "config",
    },
    # 安装 src/ 下的所有包 + 根目录的 config 包
    packages=find_packages(where="src") + ["config"],
    include_package_data=True,
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.23.0",
        "pyyaml>=6.0",
        "python-dotenv>=1.0.0",
        "akshare>=1.10.0",
        "tushare>=1.2.0",
        "matplotlib>=3.6.0",
        "pyarrow>=14.0.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0.0"],
        "ml": ["scikit-learn>=1.3.0", "xgboost>=1.7.0", "lightgbm>=3.3.0"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
