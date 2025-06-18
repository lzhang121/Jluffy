# from DrissionPage import ChromiumPage

# page = ChromiumPage()
# page.get('http://localhost:8088/index.html')
# # id属性定位
# tag1 = page.ele('@id=one')  # 获取第一个id为one的元素

# # 文本定位
# tag2 = page.ele('@text()=第一行')  # 获取第一个文本为“第一行”的元素

# # 当需要多个条件同时确定一个元素时，每个属性用'@@'开头。
# tag3 = page.ele('@@class=p_cls@@text()=第三行')  # 查找class为p_cls且文本为“第三行”的元素

# # 当需要以或关系条件查找元素时，每个属性用'@|'开头。
# tag4 = page.eles('@|id=row1@|id=row2')  # 查找所有id为row1或id为row2的元素

# # 表示模糊匹配，匹配含有指定字符串的文本或属性。
# tag5 = page.eles('@id:ow')  # 获取id属性包含'ow'的元素

# # 表示匹配开头，匹配开头为指定字符串的文本或属性。
# tag6 = page.eles('@id^row')  # 获取id属性以'row'开头的元素

# # 表示匹配结尾，匹配结尾为指定字符串的文本或属性。
# tag7 = page.ele('@id$w1')  # 获取id属性以'w1'结尾的元素

# for i in range(1, 8):
#     print(f"tag{i}: ", eval(f'tag{i}'))
# 关闭浏览器

# # id属性定位
# ele1 = page.ele("#one")
# ele2 = page.ele("#=one")
# ele3 = page.ele("#:ne")
# ele4 = page.ele("#^on")
# ele5 = page.ele("#$ne")
# for i in range(1, 6):
#     print(f"-id ele{i}: ", eval(f'ele{i}'))

# # class属性定位, 慢
# ele6 = page.ele(".p_cls")
# ele7 = page.ele(".=p_cls")
# ele8 = page.ele(".:cls")
# ele9 = page.ele(".^_cls")
# ele10 = page.ele(".p_cls$")
# for i in range(6, 11):
#     print(f"-class ele{i}: ", eval(f'ele{i}'))

# # 文本定位
# ele11 = page.ele("text=第一行")
# ele12 = page.ele("text:第一行")
# ele13 = page.ele("text^第一行")
# ele14 = page.ele("text$第一行")

# for i in range(11, 15):
#     print(f"-text ele{i}: ", eval(f'ele{i}'))

# # tag 定位
# ele15 = page.ele("tag=div")
# ele16 = page.ele("tag:p@class=p_cls")
# ele17 = page.ele("tag:p@@class=p_cls@@text()=第二行")
# ele18 = page.ele("tag:p@|class=p_cls@|text()=第二行")
# for i in range(15, 19):
#     print(f"-tag ele{i}: ", eval(f'ele{i}'))

# # xpath 定位
# ele19 = page.ele("xpath=//*[@id='one']")
# ele20 = page.ele("xpath=//div[@id='one']")
# ele21 = page.ele("xpath=//div[@id='one' and @class='p_cls']")
# ele22 = page.ele("xpath=//div[@id='one' or @class='p_cls']")
# ele23 = page.ele("xpath=//div[contains(@id,'one')]")
# ele24 = page.ele("xpath=//div[starts-with(@id,'one')]")
# ele25 = page.ele("xpath=//div[ends-with(@id,'one')]")
# for i in range(19, 26):
#     print(f"-xpath ele{i}: ", eval(f'ele{i}'))
# # css 定位, 太慢
# ele26 = page.ele("css=#one")
# ele27 = page.ele("css=div#one")
# ele28 = page.ele("css=div#one.p_cls")
# ele29 = page.ele("css=div#one.p_cls:first-child")
# ele30 = page.ele("css=div#one.p_cls:last-child")
# ele31 = page.ele("css=div#one.p_cls:nth-child(2)")
# ele32 = page.ele("css=div#one.p_cls:nth-of-type(2)")
# ele33 = page.ele("css=div#one.p_cls:nth-last-child(2)")
# for i in range(26, 34):
#     print(f"-css ele{i}: ", eval(f'ele{i}'))

# 通过xpath获取元素列表
# eles = page.eles('xpath://div/p[contains(@id,"row")]')
# for ele in eles:
#     print(ele.text, ele.link)
# page.quit()


# from DrissionPage import SessionPage

# page = SessionPage()
# page.get('https://www.baidu.com')
# eles = page.ele('#s-top-left').eles('t:a')
# print(eles.get.texts())  # 获取所有元素的文本
# print(eles.get.links())  # 获取所有元素的链接
# print(eles.get.attrs("class"))  # 获取所有元素的指定属性值

# # 导入
# from DrissionPage import SessionPage
# # 创建页面对象
# page = SessionPage()
# # 访问网页
# page.get('https://gitee.com/explore/all')
# # 在页面中查找元素
# items = page.eles('tag:h3')
# # 遍历元素
# for item in items[:-1]:
#     # 获取当前<h3>元素下的<a>元素
#     lnk = item('tag:a')
#     # 打印<a>元素文本和href属性
#     print(lnk.text, lnk.link)


# from DrissionPage import SessionPage

# page = SessionPage()
# url = 'https://game.51.com/search/action/game/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
# cookies = {'name': 'value'}
# # proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
# param = {"q": '传奇'}
# page.get(url, headers=headers, cookies=cookies, params=param, proxies=None)
# print(page.html, page.title)


from DrissionPage import SessionPage

page = SessionPage()
url = 'http://www.cpta.com.cn/category/search'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
cookies = {'name': 'value'}
# proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
data = {"keywords": '财务', '搜索': '搜索'}
page.post(url, headers=headers, cookies=cookies, data=data, proxies=None)
print(page.html, page.title)
