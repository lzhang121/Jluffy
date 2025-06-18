require("./loader")
require("./mod1")
require("./mod2")

console.log(window.loader)
i = window.loader(145)
o = window.loader.n(i)
function get_sign(time){
    n = `timestamp=${time}&secret=KHVheWluZ18zZWNyZXRfYXBB`
    return o()(n)
}