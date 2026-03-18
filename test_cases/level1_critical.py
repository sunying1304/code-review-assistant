# 质量等级：极差（Level 1）
# 预期分数：0-40
# 问题：SQL注入、硬编码密钥、裸except、同步阻塞、全局变量滥用

import os, sys, time
import sqlite3

# 硬编码密钥（Critical - Security）
API_KEY = "sk-prod-abc123456789secret"
DB_PASSWORD = "admin123"

# 全局可变状态（Warning - Best Practice）
user_cache = []

def login(username, password):
    # SQL 注入漏洞（Critical - Security）
    conn = sqlite3.connect("app.db")
    c = conn.cursor()
    query = "SELECT * FROM users WHERE name='" + username + "' AND pass='" + password + "'"
    c.execute(query)
    result = c.fetchone()
    conn.close()
    return result

def get_all_users():
    # O(n²) 查找重复（Warning - Performance）
    conn = sqlite3.connect("app.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    duplicates = []
    for i in range(len(users)):
        for j in range(len(users)):
            if users[i][0] == users[j][0] and i != j:
                duplicates.append(users[i])
    return users, duplicates

def process_data(data):
    # 裸 except 吞掉所有异常（Critical - Best Practice）
    try:
        result = int(data) / 0
        return result
    except:
        pass

def render_html(user_input):
    # XSS 漏洞（Critical - Security）
    return "<div>" + user_input + "</div>"

# 同步阻塞主线程（Warning - Performance）
time.sleep(5)
print("App started")
