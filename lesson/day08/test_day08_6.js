// 原始函数
const originalLog = console.log;

// Hook: 重写 log
console.log = function (...args) {
  originalLog('[Hooked]', ...args);
  // 你可以加更多逻辑，比如上报日志
};

console.log('hello');  // 输出: [Hooked] hello
