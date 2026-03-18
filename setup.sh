#!/bin/bash
set -e

echo "=============================="
echo " 代码 Review 助手 - 环境安装"
echo "=============================="

# 创建虚拟环境
VENV_DIR="$(dirname "$0")/venv"
if [ ! -d "$VENV_DIR" ]; then
  echo "[...] 创建 Python 虚拟环境..."
  python3 -m venv "$VENV_DIR"
fi
echo "[OK] 虚拟环境就绪：$VENV_DIR"

# 激活并安装依赖
source "$VENV_DIR/bin/activate"
echo "[...] 安装 Python 依赖（首次可能需要几分钟）..."
pip install --upgrade pip -q
pip install -r "$(dirname "$0")/requirements.txt" -q
echo "[OK] 依赖安装完成"

# 检查 .env 配置
ENV_FILE="$(dirname "$0")/.env"
if [ ! -f "$ENV_FILE" ]; then
  cp "$(dirname "$0")/.env.example" "$ENV_FILE"
  echo ""
  echo "[警告] 已创建 .env 文件，请先配置通义千问 API Key："
  echo "  编辑文件：$ENV_FILE"
  echo "  将 DASHSCOPE_API_KEY=your_api_key_here 替换为真实 Key"
  echo ""
elif grep -q "your_api_key_here" "$ENV_FILE"; then
  echo ""
  echo "[警告] 请先配置通义千问 API Key："
  echo "  编辑文件：$ENV_FILE"
  echo "  将 DASHSCOPE_API_KEY=your_api_key_here 替换为真实 Key"
  echo ""
fi

echo "=============================="
echo " 安装完成！启动服务请执行："
echo "   bash start.sh          # 本地访问"
echo "   bash start_public.sh   # 生成公网地址（供同事访问）"
echo "=============================="
