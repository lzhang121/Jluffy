import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    # Referer啥意思？不讲，后面单独讲
    'Referer': 'https://www.icve.com.cn/portal_new/course/course.html?keyvalue=%E6%97%85%E6%B8%B8'
}

url = 'https://www.icve.com.cn/portal/course/getNewCourseInfo'
data = {
    "kczy": "",
    "order": "",
    "printstate": "",
    "keyvalue": "旅游"
}
response = requests.post(url=url, headers=headers, data=data)

# 获取响应数据
# json()可以将响应数据进行反序列化
page_text = response.json()

for dic in page_text['list']:
    title = dic['Title']
    name = dic['TeacherDisplayname']
    print(title, name)
