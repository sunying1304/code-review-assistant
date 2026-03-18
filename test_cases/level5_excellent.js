// 质量等级：优秀（Level 5）
// 预期分数：90-100
// 几乎无问题：完整类型注释、错误处理、安全实践、清晰命名

const API_BASE_URL = process.env.REACT_APP_API_URL ?? '';

const DISCOUNT_THRESHOLD = 1000;
const DISCOUNT_RATES = Object.freeze({ high: 0.85, low: 0.95 });

/**
 * 获取用户信息
 * @param {string} userId - 用户 ID（非空字符串）
 * @returns {Promise<Object>} 用户数据对象
 * @throws {TypeError} 当 userId 不合法时
 * @throws {Error} 当网络请求失败时
 */
async function getUser(userId) {
  if (!userId || typeof userId !== 'string') {
    throw new TypeError('userId 必须是非空字符串');
  }
  const url = `${API_BASE_URL}/users/${encodeURIComponent(userId)}`;
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`获取用户失败，状态码: ${response.status}`);
  }
  return response.json();
}

/**
 * 安全渲染文本内容（防止 XSS）
 * @param {string} message - 要显示的文本
 * @param {string} containerId - 容器元素 ID
 */
function renderMessage(message, containerId) {
  const container = document.getElementById(containerId);
  if (!container) {
    console.warn(`容器 #${containerId} 不存在`);
    return;
  }
  container.textContent = String(message);
}

/**
 * 筛选激活状态的条目名称
 * @param {Array<{active: boolean, name: string}>} items
 * @returns {string[]}
 */
function getActiveItemNames(items) {
  return items
    .filter(item => item.active === true)
    .map(item => item.name);
}

/**
 * 计算折扣后价格
 * @param {number} price - 原始价格（正数）
 * @returns {number} 折扣后价格
 */
function calculateDiscountedPrice(price) {
  if (typeof price !== 'number' || price < 0) {
    throw new TypeError('price 必须是非负数');
  }
  const rate = price > DISCOUNT_THRESHOLD
    ? DISCOUNT_RATES.high
    : DISCOUNT_RATES.low;
  return price * rate;
}

export { getUser, renderMessage, getActiveItemNames, calculateDiscountedPrice };
