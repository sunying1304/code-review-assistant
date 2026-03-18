# 质量等级：较差（Level 2）
# 预期分数：40-60
# 问题：MD5密码哈希、缺少类型注解、命名不规范、无日志

import hashlib

SECRET = "my_secret_key"

def hashpwd(p):
    # 使用不安全的 MD5（Warning - Security）
    return hashlib.md5(p.encode()).hexdigest()

def find_dups(lst):
    # 变量命名不清晰（Info - Readability）
    r = []
    s = set()
    for x in lst:
        if x in s:
            r.append(x)
        s.add(x)
    return r

class usermgr:
    # 类名不符合 PEP8（Warning - Readability）
    def __init__(self):
        self.u = {}

    def add(self, n, p):
        # 参数名过短，无类型注解（Info - Readability）
        if n in self.u:
            return False
        self.u[n] = hashpwd(p)
        return True

    def check(self, n, p):
        if n not in self.u:
            return False
        # 直接比较哈希，无 timing-safe 比较（Warning - Security）
        return self.u[n] == hashpwd(p)

    def getall(self):
        # 直接暴露内部字典（Warning - Best Practice）
        return self.u
