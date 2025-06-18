function User(name,pwd){
    this.userName = name;
    this.pwd = pwd;
    this.regist = function(){
        console.log(this.name+"在注册")
    }
}
//类似于类属性
User.prototype.address = "BJ";
User.prototype.gender = "male";
//类似于类方法
User.prototype.login = function login(username, password){
    console.log(`${username}在登录`);
}
let u1 = new User('jay','123');
let u2 = new User('tom','456');
// //实例对象共享原型对象存储的内容
u1.login('jay','123');
u2.login('tom','456');
console.log(u1.address,u1.gender);
u2.address = "SH"; //实例对象可以覆盖原型对象的属性
u2.pwd = "789"; //实例对象可以覆盖实例对象的属性
console.log(u1.pwd,u2.pwd);
