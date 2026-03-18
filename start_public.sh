#!/bin/bash

# 代码 Review 助手 - 公网访问启动脚本
# 使用 Cloudflare Tunnel 生成临时公网地址，供同事访问
# 无需注册账号，免费使用，每次启动地址不同

echo "========================================="
echo "  代码 Review 助手 - 公网访问模式"
echo "========================================="
echo ""

cd "$(dirname "$0")"

# 检查虚拟环境
VENV_DIR="./venv"
if [ ! -d "$VENV_DIR" ]; then
  echo "❌ 虚拟环境不存在，请先运行：bash setup.sh"
  exit 1
fi

# 检查 cloudflared
if ! command -v /opt/homebrew/bin/cloudflared &> /dev/null; then
  echo "❌ cloudflared 未安装，正在安装..."
  /opt/homebrew/bin/brew install cloudflared
  echo "✅ cloudflared 安装完成"
fi

# 启动本地服务（后台运行）
echo "✓ 启动本地服务（端口 8001）..."
source "$VENV_DIR/bin/activate"
uvicorn app:app --host 0.0.0.0 --port 8001 > /tmp/code_review_server.log 2>&1 &
LOCAL_PID=$!

# 等待服务就绪
sleep 4

# 验证服务是否启动成功
if ! curl -s http://localhost:8001/ > /dev/null 2>&1; then
  echo "❌ 本地服务启动失败，请检查 .env 配置和依赖"
  cat /tmp/code_review_server.log
  kill $LOCAL_PID 2>/dev/null
  exit 1
fi
echo "✓ 本地服务启动成功"

echo ""
echo "✓ 启动 Cloudflare Tunnel..."
echo ""
echo "================================================"
echo "  公网地址将在下方显示（trycloudflare.com）"
echo "  将该地址发给同事即可直接访问"
echo "  按 Ctrl+C 停止服务并关闭公网访问"
echo "================================================"
echo ""

# 启动 Cloudflare Tunnel（前台运行，显示公网地址）
/opt/homebrew/bin/cloudflared tunnel --url http://localhost:8001

# 退出时清理本地服务
kill $LOCAL_PID 2>/dev/null
echo ""
echo "✓ 服务已停止"
