function hookFunction(obj, fnName, before, after) {
    const original = obj[fnName];

    obj[fnName] = function (...args) {
      before && before(...args);
      const result = original.apply(this, args);
      after && after(result);
      return result;
    };
  }

  // 使用示例
  hookFunction(Math, 'max',(...args) => console.log('调用前:', args),(res) => console.log('调用后:', res));

  Math.max(1, 5, 3); // 输出调用前、调用后日志
