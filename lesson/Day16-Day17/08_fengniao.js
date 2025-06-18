
require("./09 loader")
require("./10 mod1")



r = window.loader(390)
a = window.loader(391)

function get_sign(t) {
    var e = r(t);
    return encodeURIComponent(a.stringify(e))
}

/*t = "timestamp=1745656397603&secret=KHVheWluZ18zZWNyZXRfYXBB"
console.log(get_sign(t))*/
