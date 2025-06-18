//判断对象类型typeof和Object.prototype.toString.call（Object原型对象）
console.log('数字1',typeof 1);
console.log("字符串1",typeof "1");
console.log('空对象{}',typeof {});
console.log('布尔true',typeof true);
console.log('空数组[]',typeof []);
console.log('null空',typeof null);
console.log('undefined',typeof undefined);
console.log('函数function (){}',typeof function (){});
//发现null和空数组[]类型都是object类型（无法区分具体类型）
console.log("=================================")
console.log(Object.prototype.toString.call(1));
console.log(Object.prototype.toString.call("1"));
console.log(Object.prototype.toString.call({}));
console.log(Object.prototype.toString.call(true));
console.log(Object.prototype.toString.call([]));
console.log(Object.prototype.toString.call(null));
console.log(Object.prototype.toString.call(undefined));
console.log(Object.prototype.toString.call(function () {}));

// //创建新对象，设置其原型对象为window（在node环境下可能需要伪装浏览器环境下的对象）
// a = Object.create(global)
// a.__proto__ === window //true
console.log("=================================")
//判断对象自身属性中是否具有指定的属性
function func(){
    this.name="bobo";
    this.getAge=function(){}
};
f = new func();
f.hasOwnProperty('name'); //true
f.hasOwnProperty('getAge'); //true
f.hasOwnProperty('toString'); //false

//获取指定对象上一个自有属性对应的属性描述符
Object.getOwnPropertyDescriptor(f,'name');
//获取指定对象上所有属性对应的属性描述符
Object.getOwnPropertyDescriptors(f);
/*
	属性描述符是一组用于精确定义和描述对象属性的特性的集合(属性描述符也是一个对象)。通过属性描述符，开发者可以指定一个属性是否可被修改、删除、枚举或者通过特定的函数来获取和设置其值。
*/


//获取实例对象的原型对象
Object.getPrototypeOf(f);
Object.getPrototypeOf(f) === f.__proto__ ;//true

//设置一个指定的对象的原型(可以对一个已经存在的对象重新设置其原型对象)
Object.setPrototypeOf(f,Object.__proto__) //f对象的原型对象设置成了window的原型对象


//defineProperty直接在一个对象上定义一个新属性，然后可指定新属性的属性描述的，并返回此对象。
let User = {
    "name":"小明",
}//创建一个User对象
//给对象添加两个成员
User.age = 10;
User["age"] = 20;
//给对象定义一个新属性且设置其属性描述符（属性描述符可分为：数据描述符和存取描述符）此时使用数据描述符。
	//参数1：对象。参数2：属性名。参数3：属性描述的
Object.defineProperty(User, "height", {
    enumerable:true, //该属性是否可遍历
    configurable:true,//该属性是否可配置:决定该属性是否可以被删除或修改其属性描述符。
    value:160, //属性的值
    writable:false //该属性的值是否可以通过赋值运算符改变
});
//对象属性遍历,如果某个属性的文件描述符中的enumerable:false则无法遍历出该属性
for (const userKey in User) {
    console.log(userKey);
}
//存取描述符
let Stu = {
    "name":"小红",
}//创建一个Stu对象
let temp = null;//临时变量
//给Stu对象定义一个新属性score，且设置其属性描述符
Object.defineProperty(Stu, "score", {
    enumerable:true,
    configurable:true,
    get:function (){// 当获取属性值是调用
        console.log("正在获取值");
        return temp;
    },
    set:function (value){// 当对属性进行赋值操作时调用
        console.log("正在设置值");
        temp = value;
    }
});
console.log(User.score);
User.score = 100;
console.log(User.score);
/*
	属性描述符注意事项：属性描述符分为两类：数据描述符和存取描述符。数据描述符包含value、writable、enumerable和configurable这些属性。存取描述符包含get、set、enumerable和configurable。两者不能混用，即一个描述符如果是数据描述符就不能包含get或set，反之亦然。
*/