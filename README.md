# 代码 Review 助手

一个基于 AI 的代码评审工具，支持 Python 和 JavaScript，从可读性、性能、安全性、最佳实践四个维度自动分析代码质量。

## 功能特性

- **多维度分析**：可读性 / 性能 / 安全性 / 最佳实践
- **问题定位**：精确到行号，快速定位问题
- **严重等级**：Critical（🔴）/ Warning（🟡）/ Info（🔵）三级分类
- **修复建议**：每个问题附带改进建议和修复后的代码示例
- **综合评分**：0-100 分评分，对应优秀/良好/中等/较差/极差五个等级
- **内置示例**：5 个不同质量级别的示例代码，方便快速体验

## 快速开始

### 环境要求

- Python 3.10+
- 通义千问 API Key（[申请地址](https://dashscope.aliyun.com/)）

### 安装依赖

```bash
cd code-review
pip install -r requirements.txt
```

### 配置 API Key

```bash
cp .env.example .env
# 编辑 .env，填入你的通义千问 API Key
```

`.env` 内容：

```
DASHSCOPE_API_KEY=your_api_key_here
```

### 启动服务

```bash
uvicorn app:app --reload --port 8001
```

浏览器打开：[http://localhost:8001](http://localhost:8001)

## 使用方法

1. 选择代码语言（Python / JavaScript）
2. 在输入框中粘贴代码，或点击示例按钮加载内置示例
3. 点击「开始 Review」
4. 查看评分和各维度问题列表
5. 点击问题卡片查看修复建议和示例代码

## 评分规则

| 分数区间 | 等级 | 说明 |
|----------|------|------|
| 90-100 | 优秀 | 几乎无问题，可直接合入 |
| 75-89 | 良好 | 有少量 Info/Warning，建议修复后合入 |
| 60-74 | 中等 | 有较多 Warning，需要修复主要问题 |
| 40-59 | 较差 | 有 Critical 或大量 Warning，必须修复 |
| 0-39 | 极差 | 存在严重安全漏洞，禁止合入 |

扣分规则：
- 每个 Critical：-15 分
- 每个 Warning：-5 分
- 每个 Info：-1 分

## 项目结构

```
code-review/
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
    ├── level1_critical.py  # 极差（0-39）
    ├── level2_poor.py      # 较差（40-59）
    ├── level3_medium.js    # 中等（60-74）
    ├── level4_good.py      # 良好（75-89）
    └── level5_excellent.js # 优秀（90-100）
```

## 技术栈

- **后端**：Python + FastAPI
- **前端**：原生 HTML/CSS/JavaScript（无框架依赖）
- **AI 模型**：通义千问 qwen-long

## 评审维度说明

详见 [REVIEW_STANDARDS.md](REVIEW_STANDARDS.md)
