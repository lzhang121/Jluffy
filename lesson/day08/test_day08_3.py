import execjs

new_date = execjs.eval("new Date")
print(new_date)

date_now = execjs.eval("Date.now()")
print(date_now)
