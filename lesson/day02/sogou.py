import requests

url = "https://sogou.com/web?query=tiki&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sourceid=9_01_03&sessiontime=1750230341516"

payload = {}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://sogou.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Cookie': 'ABTEST=0|1750229503|v17; IPLOC=JP; SUID=C3C2D86F3EA7A20B00000000685261FF; cuid=AAGCvGw4VAAAAAuipyOMMgEAMQQ=; SUV=1750229503514181; SNUID=6E6F76C1AEA8997DEA9AEFD5AEA53F94'
}

response = requests.request("GET", url, headers=headers, data=payload)

page_text = response.text

with open('sogou.html', 'w') as fp:
    fp.write(page_text)
