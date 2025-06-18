# Webpack逆向

Webpack是一个现代的静态模块打包工具，它主要用于前端开发中的模块化打包和构建。通过Webpack，开发者可以将多个模块（包括JavaScript、CSS、图片等）进行打包，生成优化后的静态资源文件，以供在浏览器中加载和运行。

Webpack的主要功能和特点包括：

1. 模块化支持：Webpack将应用程序拆分为多个模块，通过模块化的方式管理和加载依赖关系。它支持CommonJS、ES module、AMD等多种模块化规范，并且能够将这些模块打包成最终的静态资源文件。
2. 打包和压缩：Webpack可以将多个模块打包成一个或多个最终的静态资源文件。它支持对JavaScript、CSS、图片等资源进行压缩、合并和优化，以减小文件大小，提升加载速度和性能。
3. 资源加载管理：Webpack可以处理各种类型的资源文件，例如JavaScript、CSS、图片、字体等。通过加载器（Loader）的配置，Webpack可以对这些资源文件进行转换和处理，使其能够被应用程序正确地引用和加载。

```js
/*
!function(形参){加载器}([模块1，模块2,...])

!function(形参){加载器}({"k1":"模块1","k2":"模块2"}) 
*/
```

```js
window = global;
!function (e) {
    var t = {};

    function n(r) {
        if (t[r])
            return t[r].exports;
        var o = t[r] = {
            i: r,
            l: !1,
            exports: {}
        };
        e[r].call(o.exports, o, o.exports, n);
        return o.exports.exports; 
    }

    window.loader = n;

    // n("1002");
}([ function () {
        console.log("foo");
        this.exports = 100; 
    },
    function () {
        console.log("bar");
        this.exports = 200;
    }]
);

console.log(window.loader(0));
console.log(window.loader(1));
```

```js
window = global;
!function (e) {
    var t = {};

    function n(r) {
        if (t[r])
            return t[r].exports;
        var o = t[r] = {
            i: r,
            l: !1,
            exports: {}
        };
        e[r].call(o.exports, o, o.exports, n);
        return o.exports.exports; // 返回 o.exports.exports，而不是整个 o.exports 对象
    }
    
    window.loader = n;

    // n("1002");
}({
    "1001": function () {
        console.log("foo");
        this.exports = 100; // 直接修改 exports 变量
    },
    "1002": function () {
        console.log("bar");
        this.exports = 200;
    }
});

console.log(window.loader("1001"));
```

