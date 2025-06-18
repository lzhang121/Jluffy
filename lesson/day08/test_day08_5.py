# 只简单试了三种， 在windows下
import execjs
import os
import time

# 先用JScript
os.environ["EXECJS_RUNTIME"] = "JScript"
print(execjs.get().name)

time1 = time.time()
for i in range(100):
    execjs.eval("new Date")
print(time.time() - time1)

# 切换环境 使用Nodejs
os.environ["EXECJS_RUNTIME"] = "Node"
print(execjs.get().name)

time2 = time.time()
for l in range(100):
    execjs.eval("new Date")
print(time.time() - time2)

# 打印的结果为：
# JScript
# 4.70900011063
# Node.js(V8)
# 27.501999855

# 在ubuntu下试的是PhantoJS ， 结果竟然高达 30+ S
