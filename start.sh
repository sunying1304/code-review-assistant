#!/bin/bash
set -e

cd "$(dirname "$0")"

VENV_DIR="./venv"
if [ ! -d "$VENV_DIR" ]; then
  echo "[错误] 虚拟环境不存在，请先运行：bash setup.sh"
  exit 1
fi

source "$VENV_DIR/bin/activate"

echo "=============================="
echo " 代码 Review 助手"
echo " 浏览器打开：http://localhost:8001"
echo " 按 Ctrl+C 停止服务"
echo "=============================="

uvicorn app:app --host 0.0.0.0 --port 8001
