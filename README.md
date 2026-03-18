# 代码 Review 助手

**🌐 在线访问：[https://organization-quarters-subsection-vitamin.trycloudflare.com](https://organization-quarters-subsection-vitamin.trycloudflare.com)**

一个基于 AI 的代码评审工具，支持 Python 和 JavaScript，从可读性、性能、安全性、最佳实践四个维度自动分析代码质量。

## 功能特性

- **多维度分析**：可读性 / 性能 / 安全性 / 最佳实践
- **问题定位**：精确到行号，快速定位问题
- **严重等级**：Critical（🔴）/ Warning（🟡）/ Info（🔵）三级分类
- **修复建议**：每个问题附带改进建议和修复后的代码示例
- **综合评分**：0-100 分，对应优秀/良好/中等/较差/极差五个等级
- **内置示例**：5 个不同质量级别的示例代码，方便快速体验

---

## 快速开始

### 环境要求

- macOS（Apple Silicon 或 Intel）
- Python 3.9+
- 通义千问 API Key（[免费申请](https://dashscope.aliyun.com/)）

### 第一步：安装依赖

```bash
cd code-review
bash setup.sh
```

### 第二步：配置 API Key

编辑 `.env` 文件（`setup.sh` 会自动创建），填入通义千问 API Key：

```
DASHSCOPE_API_KEY=your_api_key_here
```

### 第三步：启动服务

**本地使用（仅自己访问）：**

```bash
bash start.sh
```

浏览器打开：[http://localhost:8001](http://localhost:8001)

**公网访问（供同事使用）：**

```bash
bash start_public.sh
```

启动后终端会显示一个 `trycloudflare.com` 的公网地址，将该地址发给同事即可直接访问，无需任何账号注册，完全免费。

> 注意：每次启动地址不同；关闭终端后地址失效。

---

## 使用方法

1. 选择代码语言（Python / JavaScript）
2. 粘贴代码，或点击示例按钮加载内置示例
3. 点击「开始 Review」
4. 查看评分和各维度问题列表
5. 点击问题卡片查看修复建议和示例代码

---

## 评分规则

| 分数区间 | 等级 | 说明 |
|----------|------|------|
| 90-100 | 优秀 | 几乎无问题，可直接合入 |
| 75-89 | 良好 | 有少量 Info/Warning，建议修复后合入 |
| 60-74 | 中等 | 有较多 Warning，需要修复主要问题 |
| 40-59 | 较差 | 有 Critical 或大量 Warning，必须修复 |
| 0-39 | 极差 | 存在严重安全漏洞，禁止合入 |

扣分规则：每个 Critical -15 分 / 每个 Warning -5 分 / 每个 Info -1 分

---

## 项目结构

```
code-review/
├── setup.sh                # 一键安装依赖
├── start.sh                # 本地启动
├── start_public.sh         # 公网访问启动（Cloudflare Tunnel）
├── app.py                  # FastAPI 主应用（端口 8001）
├── requirements.txt        # Python 依赖
├── .env                    # API Key 配置（不提交到 git）
├── .env.example            # 配置模板
├── REVIEW_STANDARDS.md     # 评审标准详细说明
├── static/
│   └── index.html          # 单页前端
├── utils/
│   └── reviewer.py         # 调用通义千问进行代码评审
└── test_cases/             # 5 个不同质量级别的测试代码
    ├── README.md
    ├── level1_critical.py  # 极差（得分 0-39）
    ├── level2_poor.py      # 较差（得分 40-59）
    ├── level3_medium.js    # 中等（得分 60-74）
    ├── level4_good.py      # 良好（得分 75-89）
    └── level5_excellent.js # 优秀（得分 90-100）
```

---

## 技术栈

- **后端**：Python + FastAPI
- **前端**：原生 HTML/CSS/JavaScript（无框架依赖）
- **AI 模型**：通义千问 qwen-long
- **公网穿透**：Cloudflare Tunnel（免费，无需注册）

## 评审维度说明

详见 [REVIEW_STANDARDS.md](REVIEW_STANDARDS.md)
