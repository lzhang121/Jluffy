function User(name,pwd){
    this.userName = name;
    this.pwd = pwd;
    this.regist = function(){
        console.log(this.name+"在注册")
    }
}