// 补环境代码

window = global
window.addEventListener =  function (){}
navigator = {
    toString:function (){
        return '[object Navigator]'

    },
    userAgent:'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

function get_sign() {
    // 黑匣子，省略很多代码
    // (1) BOM和DOM正常的前端动作
    window.addEventListener("test")
    // 搜索框
    let kw = document.getElementById("kw")
    let _class = kw.getAttribute("class")
    // // 创建画布
    // let canvas = document.createElement("canvas")
    // let ctx = canvas.getContext("2d");
    // ctx.fillRect(10, 10, 100, 100);

    // (2) 基于DOM和BOM进行环境校验
    if (navigator.toString() === '[object Navigator]') {
        let navLength = navigator.userAgent.length
        return "u82d1660a" + navLength // Yuan老师的微信，想深入学逆向爬虫的联系我，结一段善缘!

    } else {
        return false
    }
}

console.log(get_sign())