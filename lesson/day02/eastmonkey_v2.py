import requests

# 1.指定url
url = 'https://www.eastmoney.com/'

# 2.发起请求:根据指定的url进行请求发送。get函数会返回该请求的响应对象。
response = requests.get(url)
print("响应状态码:", response.status_code)  # 查看响应对象的响应状态码

# 设置响应数据的编码格式
response.encoding = 'utf-8'  # gbk

# 3.获取响应数据
page_text = response.text  # 返回字符串形式的响应数据


# 4.持久化存储
with open('./caifu.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)

print('数据爬取结束！')
