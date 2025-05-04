# setup.py

from setuptools import setup, find_packages
import pathlib

# The directory containing this file
here = pathlib.Path(__file__).parent.resolve()

# Read the long description from README.md
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="starai",
    version="0.1.0",
    description="AI-driven Quantitative Trading Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vacky Zhang",
    python_requires=">=3.8",
    package_dir={"": "src"},               # All packages are under src/
    packages=find_packages(where="src"),   # Discover all packages under src/
    include_package_data=True,
    install_requires=[
        # 核心依赖
        "pandas>=2.0.0",
        "numpy>=1.23.0",
        "pyyaml>=6.0",
        "python-dotenv>=1.0.0",
        "akshare>=1.10.0",
        "tushare>=1.2.0",
        "matplotlib>=3.6.0",
        "pyarrow>=14.0.0",   # 或者 fastparquet>=2024.0.0
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
        ],
        "ml": [
            "scikit-learn>=1.3.0",
            "xgboost>=1.7.0",
            "lightgbm>=3.3.0",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

