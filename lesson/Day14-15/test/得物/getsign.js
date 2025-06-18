require("./env")
require("./loader")
require("./mod1")

var t = {
    "pickRuleId": 644443,
    "pageNum": 1,
    "pageSize": 24,
    "filterUnbid": true,
    "showCspu": true
}

c = window.loader("aCH8");
l = (window.loader("cnSC"),
    window.loader("doui"),
    window.loader("pLtp"))
f = window.loader.n(c)
s = window.loader.n(l)

function getSign(e) {
    return f()("".concat(e ? s()(e).sort().reduce(function (t, n) {
        return "".concat(t).concat(n).concat(e[n])
    }, "") : "", "048a9c4943398714b356a696503d2d36"))
}


// s = 'U2Fs@!#X19kvTcThAZAIg275tvafZ1i'
// console.log(s.length)