// 质量等级：中等（Level 3）
// 预期分数：60-75
// 问题：同步 XHR、var 声明、innerHTML、缺少错误处理

var BASE_URL = "https://api.example.com";

// 使用同步 XHR 阻塞主线程（Warning - Performance）
function getUserSync(id) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", BASE_URL + "/users/" + id, false); // false = 同步
  xhr.send();
  return JSON.parse(xhr.responseText);
}

// 使用 innerHTML 存在 XSS 风险（Warning - Security）
function showMessage(msg) {
  document.getElementById("msg").innerHTML = msg;
}

// var 声明，无块级作用域（Info - Best Practice）
function processItems(items) {
  var result = [];
  for (var i = 0; i < items.length; i++) {
    var item = items[i];
    if (item.active == true) { // 使用 == 而非 ===（Info - Best Practice）
      result.push(item.name);
    }
  }
  return result;
}

// 缺少错误处理（Warning - Best Practice）
async function fetchData(url) {
  const response = await fetch(url);
  const data = await response.json();
  return data;
}

// 魔法数字（Info - Readability）
function calculateDiscount(price) {
  if (price > 1000) {
    return price * 0.85;
  }
  return price * 0.95;
}
