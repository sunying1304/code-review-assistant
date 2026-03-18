# 测试用例说明

共 5 个测试用例，覆盖不同质量等级，用于验证 Review 工具的分析能力。

| 文件 | 语言 | 质量等级 | 预期分数 | 主要问题 |
|------|------|----------|----------|----------|
| level1_critical.py | Python | 极差 | 0-40 | SQL注入、硬编码密钥、裸except |
| level2_poor.py | Python | 较差 | 40-60 | MD5密码、O(n²)算法、无类型注解 |
| level3_medium.js | JavaScript | 中等 | 60-75 | 同步XHR、var声明、无错误处理 |
| level4_good.py | Python | 良好 | 75-90 | 小问题：缺少文档、日志不完整 |
| level5_excellent.js | JavaScript | 优秀 | 90-100 | 几乎无问题 |
