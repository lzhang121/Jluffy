# 1.导包
import execjs
# 2.创建node对象
node = execjs.get()
# 3.编译js文件返回上下文ctx对象(将js文件中的代码读取出来，被compile进行编译)
fp = open('/Users/zhanglei/git/Jluffy/lesson/day08/main.js',
          'r', encoding='utf-8')
ctx = node.compile(fp.read())
# 4.使用上下文对象ctx调用eval函数执行js文件中的指定函数即可
result = ctx.eval('P("123456")')
print(result)
