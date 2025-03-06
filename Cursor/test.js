/**
 * 获取指定范围内的随机整数
 * @param {number} min 最小值（包含）
 * @param {number} max 最大值（包含）
 * @returns {number} 随机整数
 */
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * 获取指定范围内的随机浮点数
 * @param {number} min 最小值（包含）
 * @param {number} max 最大值（不包含）
 * @returns {number} 随机浮点数
 */
function getRandomFloat(min, max) {
    return Math.random() * (max - min) + min;
}

/**
 * 从数组中随机获取一个元素
 * @param {Array} array 源数组
 * @returns {*} 随机元素
 */
function getRandomArrayElement(array) {
    return array[Math.floor(Math.random() * array.length)];
}

// 获取1到10之间的随机整数
console.log(getRandomInt(1, 10));  // 输出类似：3, 7, 10等

// 获取0到1之间的随机浮点数
console.log(getRandomFloat(0, 1));  // 输出类似：0.234567

// 从数组中随机选择元素
const fruits = ['苹果', '香蕉', '橙子', '葡萄'];
console.log(getRandomArrayElement(fruits));  // 输出类似：'香蕉'
