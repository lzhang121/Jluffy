import urllib.parse
from DrissionPage import ChromiumPage, ChromiumOptions
from DrissionPage.errors import ElementNotFoundError


# 创建 Chromium 浏览器选项
co = ChromiumOptions()
# co.headless(True)  # 启用无头模式
co.set_argument('--disable-gpu')  # 可选：禁用 GPU
co.set_argument('--no-sandbox')  # 可选：避免 Linux 权限问题
# 创建页面对象，并启动浏览器
page = ChromiumPage(co)
# 跳转到登录页面
page.get('https://t.livepocket.jp/login?acroot=header-new_p_u_nl')

# 定位到账号文本框，获取文本框元素
ele = page.ele('#email')
# 输入对文本框输入账号
ele.input('zhspark@gmail.com')

# 定位到密码文本框并输入密码
page.ele('#password').input('1QAZ2wsx3edc')
# 点击登录按钮:@attrName=value,这是根据属性和属性值进行标签定位的方式
page.ele('@value=send').click()
page.wait.ele_displayed('@value=検索', timeout=10)
# 获取登录后的页面标题
keyword = """肉フェス2025お台場【5月4日(日)アニソン＆アキバカルチャーDAY ２皿め】有料ステージ前売"""
decoded_str = urllib.parse.unquote(keyword)
url = f'https://t.livepocket.jp/event/search?word={decoded_str}&sort=0'
page.get(url)
# 等待加载完成（可选，视页面动态情况而定）
page.wait.ele_displayed('#search-result ', timeout=10)

# # 定位到所有 li.item 中的 a 标签
# link_element = page.ele('css:li.item a')  # 取第一个
# if link_element:
#     href = link_element.link
#     print(href)
# else:
#     print('未找到链接')

page.ele('#search-result ul li a figure img').click()

# page.get(href)
# 等待加载完成（可选，视页面动态情况而定）
page.wait.ele_displayed('@id:ticket-', timeout=10)
pageselect_eles = page.eles('@id^ticket-', timeout=10)
# This block of code is performing the following actions:
for pageselect_ele in pageselect_eles:
    pageselect_ele.click()
    pageselect_ele.select('1 Ticket')
    page.wait(1)
if pageselect_ele:
    pageselect_ele.click()
page.scroll.down()
page.wait(1)
page.wait.ele_displayed(
    '#submit', timeout=10)
button = page.ele(
    '#submit', timeout=10)
if button:
    button.click()
    page.wait(10)
    elements = page.eles('@text=Purchaser information', timeout=10)
    print(f'找到了 {len(elements)} 个匹配的元素')

    page.wait.ele_displayed(
        '.agreement_check_lp', timeout=10)
    notice_check_button = page.ele(
        '.agreement_check_lp', timeout=10)
    if notice_check_button:
        notice_check_button.click()

    page.wait.ele_displayed(
        '.submit-btn', timeout=10)
    pay_button = page.ele(
        '.submit-btn', timeout=10)
    if pay_button:
        pay_button.click()
else:
    print('按钮没出现')


page.quit()
