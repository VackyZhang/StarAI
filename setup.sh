#!/bin/bash

# setup.sh
echo "📦 初始化 Python 虚拟环境 .venv..."

if [ ! -d ".venv" ]; then
    echo "📁 创建新的虚拟环境..."
    python3 -m venv .venv
else
    echo "✅ 已存在 .venv，跳过创建"
fi

echo "🐍 激活虚拟环境..."
source .venv/bin/activate

echo "📦 安装 requirements.txt 中的依赖..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ 环境就绪，欢迎使用 StarAI！"
