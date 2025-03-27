from setuptools import setup, find_packages

setup(
    name="quant_ai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy", "pandas", "matplotlib", "yfinance"
    ],
)