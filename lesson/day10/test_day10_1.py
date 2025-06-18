# from DrissionPage import ChromiumPage, ChromiumOptions
# import os

# current_file_path = os.path.dirname(os.path.abspath(__file__))
# print(current_file_path)

# co = ChromiumOptions()
# co.set_argument('--start-maximized')        # Start browser maximized
# # Hide "Chrome is being controlled..." infobar
# co.set_argument('--disable-infobars')
# co.headless(True)                           # Run in headless mode if needed
# co.set_argument('--disable-gpu')            # Disable GPU acceleration
# page = ChromiumPage(co)
# page.get('https://www.baidu.com')
# page.wait(1)
# page.get_screenshot(path=current_file_path + os.sep +
#                     'screenshot.png', full_page=True)
# page.quit()


# from DrissionPage import ChromiumPage
# from DrissionPage.errors import ElementNotFoundError

# # 创建页面对象，并启动浏览器
# page = ChromiumPage()
# # 跳转到登录页面
# page.get('https://gitee.com/login#lang=zh-CN')

# # 定位到账号文本框，获取文本框元素
# ele = page.ele('#user_login')
# # 输入对文本框输入账号
# ele.input('18516891935')
# # 定位到密码文本框并输入密码
# page.ele('#user_password').input('qatest11')
# # 点击登录按钮:@attrName=value,这是根据属性和属性值进行标签定位的方式
# page.ele('@name=commit').click()
# page.wait(5)
# items = page.eles('tag:li@@class=mt-4 flex items-center')
# for item in items:
#     # 打印元素文本
#     try:
#         elem = item('tag:img', timeout=10)
#         print(elem.attrs['src'], elem.attrs['alt'])
#     except ElementNotFoundError:
#         print("未找到该元素")


# # # 访问网址,进行登录
# page.quit()


# from DrissionPage import SessionPage

# # 创建页面/请求对象
# page = SessionPage()

# # 爬取3页
# for i in range(1, 4):
#     # 访问某一页的网页
#     page.get(f'https://gitee.com/explore/all?page={i}')
#     # 获取所有开源库<a>元素列表(所有库的链接的a标签的class属性值都是一样的)
#     links = page.eles('.title project-namespace-path')
#     # 遍历所有<a>元素
#     for link in links:
#         # 打印链接信息：
#         print(link.text, link.link)


# from DrissionPage import ChromiumOptions
# from DrissionPage import WebPage

# # 创建页面对象
# page = WebPage()
# # 访问网址,进行登录
# page.get('https://gitee.com/login?redirect_to_url=%2F')
# # 定位到账号文本框，获取文本框元素
# ele = page.ele('#user_login')
# # 输入对文本框输入账号
# ele.input('18516891935')
# # 定位到密码文本框并输入密码
# page.ele('#user_password').input('qatest11')
# # 点击登录按钮:@attrName=value,这是根据属性和属性值进行标签定位的方式
# page.ele('@name=commit').click()

# # 切换到收发数据包模式
# page.change_mode()  # 切换的时候程序会在新模式重新访问当前 url。
# # 切换模式后，重新访问基于登录状态后新的url（个人主页）
# page.get('https://gitee.com/Mr_bobo')

# # 根据class属性值获取div标签，然后将该div下面class为item的元素标签批量获取
# items = page.ele('.ui middle aligned list').eles('.item')
# # 遍历获取到的元素
# for item in items:
#     # 打印元素文本
#     print(item('.content').text)
# page.quit()


# from DrissionPage import ChromiumPage

# page = ChromiumPage(42123)
# # 打印接管浏览器的page标题和访问的url
# print(page.title, page.url)
# page.quit()


# from DrissionPage import ChromiumPage, ChromiumOptions

# # 创建多个配置对象，每个指定不同的端口号和用户文件夹路径
# do1 = ChromiumOptions().set_paths(
#     local_port=9111, user_data_path=r'/Users/zhanglei/git/Jluffy/lesson/day10/tmp1')
# do2 = ChromiumOptions().set_paths(
#     local_port=9222, user_data_path=r'/Users/zhanglei/git/Jluffy/lesson/day10/tmp2')

# # 创建多个页面对象
# page1 = ChromiumPage(addr_or_opts=do1)
# page2 = ChromiumPage(addr_or_opts=do2)

# # 每个页面对象控制一个浏览器
# page1.get('https://www.baidu.com')
# page2.get('http://www.163.com')
# page1.quit()
# page2.quit()

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


# from DrissionPage import SessionPage

# page = SessionPage()
# url = 'http://www.cpta.com.cn/category/search'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
# cookies = {'name': 'value'}
# # proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
# data = {"keywords": '财务', '搜索': '搜索'}
# page.post(url, headers=headers, cookies=cookies, data=data, proxies=None)
# print(page.html, page.title)
