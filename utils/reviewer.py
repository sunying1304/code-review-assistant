import os
import json
import dashscope
from dashscope import Generation

SYSTEM_PROMPT = """你是一位资深代码审查专家，擅长 Python 和 JavaScript 代码质量分析。

请对提交的代码进行全面审查，从以下四个维度分析：
1. **可读性**：命名规范、注释质量、代码结构清晰度
2. **性能**：时间复杂度、空间复杂度、不必要的计算
3. **安全性**：SQL注入、XSS、硬编码密钥、输入验证
4. **最佳实践**：设计模式、错误处理、代码复用

每个问题必须包含：
- 行号（line）
- 维度（dimension）：readability / performance / security / best_practice
- 严重程度（severity）：critical / warning / info
- 问题描述（description）
- 改进建议（suggestion）
- 修改后的代码示例（fixed_code，仅该行或该段）

输出格式为严格的 JSON，结构如下：
{
  "summary": "整体评价（2-3句话）",
  "score": 总分（0-100整数）,
  "stats": {
    "critical": critical数量,
    "warning": warning数量,
    "info": info数量
  },
  "issues": [
    {
      "line": 行号整数,
      "dimension": "readability|performance|security|best_practice",
      "severity": "critical|warning|info",
      "description": "问题描述",
      "suggestion": "改进建议",
      "fixed_code": "修改后的代码示例"
    }
  ]
}

只输出 JSON，不要有任何其他文字。"""


def review_code(code: str, language: str) -> dict:
    """
    调用通义千问对代码进行 Review。
    返回结构化的审查结果字典。
    """
    api_key = os.getenv("DASHSCOPE_API_KEY", "")
    if not api_key or api_key == "your_dashscope_api_key_here":
        raise ValueError("请在 .env 文件中配置 DASHSCOPE_API_KEY")

    dashscope.api_key = api_key

    user_content = f"""请审查以下 {language} 代码：

```{language}
{code}
```"""

    response = Generation.call(
        model="qwen-long",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ],
        result_format="message",
        max_tokens=4096,
    )

    if response.status_code != 200:
        raise RuntimeError(f"通义千问 API 调用失败: {response.message}")

    raw = response.output.choices[0].message.content.strip()

    # 清理可能的 markdown 代码块包裹
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        # 如果解析失败，返回原始文本作为 summary
        result = {
            "summary": raw,
            "score": 0,
            "stats": {"critical": 0, "warning": 0, "info": 0},
            "issues": []
        }

    return result
