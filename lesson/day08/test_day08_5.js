// 定义函数
function add(a,b){
    console.log("add方法正在执行");
    return a+b;
}
_add = add;
let result = _add(1,2)
console.log("原函数调用后, 结果：", result);
console.log("=====================")
add = function(a,b){
	console.log("原函数调用前, 参数：", a, b);
    let result = _add(a,b)
    console.log("原函数调用后, 结果：", result);
    return result;
}
add(1,2)
console.log("=====================")
//1、创建一个对象
let user = {
    "name": "波波",
};

//2、保存原属性
_name = user.name;

//3、对象属性的hook
//defineProperty函数用来重新定义对象的属性。
//参数1：对象。参数2：属性。参数3：属性描述符
Object.defineProperty(user, "name",{
    get(){ // 获取属性值的时候执行
        console.log("正在获取属性值");
        return _name;
    },
    set(value){ // 设置属性值的时候执行
         console.log("正在设置属性值:", value);
         _name = value;
    }
});

//4、获取属性和设置属性操作

console.log("---------------------")
console.log(user.name)
console.log("---------------------")
user.name = 'Jay'
console.log("---------------------")
console.log(user.name)