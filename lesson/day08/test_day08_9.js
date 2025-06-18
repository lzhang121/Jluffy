// import fetch from 'node-fetch';
const fetch = require('node-fetch');
// Hook 示例
const originalFetch = fetch;

globalThis.fetch = async function (...args) {
  console.log('拦截 fetch 参数:', args);

  const res = await originalFetch.apply(this, args);

  const cloned = res.clone(); // clone 才能读取 body 不影响原始返回
  cloned.text().then(data => {
    console.log('响应内容:', data);
  });

  return res;
};

fetch('https://jsonplaceholder.typicode.com/todos/1');
