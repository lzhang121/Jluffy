//（1） 数组模块结构
/*!function (e) {
    var t = {};
    // 加载器函数：调度机制（调用方法）
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

    // 调用模块
    console.log(n(1))
    console.log(n(0))
}([
    function () {
        console.log("foo");
        this.exports = 100;
    },
    function () {
        console.log("bar");
        this.exports = 200;
    }
    ])*/

//（2） 对象模块结构
window = global
document = {
    cookie: ""
}
!function (e) {
    var t = {};

    // 加载器函数：调度机制（调用方法）
    function n(r) {

        if (t[r])
            return t[r].exports;
        var o = t[r] = {
            i: r,
            l: !1,
            exports: {}
        };
        // 加日志
        console.log("r:::", r)

        e[r].call(o.exports, o, o.exports, n);
        return o.exports.exports;
    }

    // 全局设置
    window.loader = n

    // 调用模块
    // console.log(n("1002"))

    // 初始化加载
    // n("1000")

}()

window.loader("1001")

