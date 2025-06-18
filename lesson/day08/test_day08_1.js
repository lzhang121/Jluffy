let a = {'name':'bobo'}; //方法1

function B(){
    this.name="bobo"
};
let b = new B(); //方法2

console.log(a);
console.log(b);