# 质量等级：良好（Level 4）
# 预期分数：75-90
# 小问题：部分函数缺少文档字符串、日志级别可优化

from typing import List, Optional
import hashlib
import secrets
import logging

logger = logging.getLogger(__name__)

DISCOUNT_THRESHOLD = 1000
DISCOUNT_HIGH = 0.85
DISCOUNT_LOW = 0.95


def hash_password(password: str) -> str:
    """使用 SHA-256 + 随机 salt 对密码哈希。"""
    salt = secrets.token_hex(16)
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{hashed}"


def verify_password(password: str, stored: str) -> bool:
    # 缺少文档字符串（Info - Readability）
    try:
        salt, hashed = stored.split(":", 1)
    except ValueError:
        return False
    return secrets.compare_digest(
        hashed,
        hashlib.sha256((salt + password).encode()).hexdigest()
    )


def find_duplicates(data: List) -> List:
    seen: set = set()
    duplicates: set = set()
    for item in data:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)


class UserManager:
    """管理用户账号的创建、验证和查询。"""

    def __init__(self):
        self._users: dict[str, str] = {}

    def add_user(self, name: str, password: str) -> bool:
        """新增用户，若用户名已存在则返回 False。"""
        if not name or not password:
            raise ValueError("用户名和密码不能为空")
        if name in self._users:
            # 日志级别可用 debug 而非 warning（Info - Best Practice）
            logger.warning("用户已存在: %s", name)
            return False
        self._users[name] = hash_password(password)
        logger.info("用户创建成功: %s", name)
        return True

    def authenticate(self, name: str, password: str) -> bool:
        """验证用户名和密码。"""
        if name not in self._users:
            return False
        return verify_password(password, self._users[name])

    def get_user_count(self) -> int:
        return len(self._users)
