const user = {
name: 'Tom',
sayHello(msg) {
    console.log(`${this.name} says ${msg}`);
}
};

const hookedUser = new Proxy(user, {
get(target, prop, receiver) {
    const orig = target[prop];
    if (typeof orig === 'function') {
    return function (...args) {
        console.log(`调用 ${prop} 前, 参数:`, args);
        const result = orig.apply(this, args);
        console.log(`调用 ${prop} 后`);
        return result;
    };
    }
    return orig;
}
});

hookedUser.sayHello('Hello Hook');  // 会打印调用前后的日志

