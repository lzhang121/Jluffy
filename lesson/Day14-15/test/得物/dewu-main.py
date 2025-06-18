import requests
import execjs
# from curl_cffi import requests
import json

cookies = {
    'PHPSESSID': '5cg43urernsaq77nvgnn9g9gt0',
    'think_var': 'zh-cn',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'PHPSESSID=5cg43urernsaq77nvgnn9g9gt0; think_var=zh-cn',
    'Origin': 'https://www.dewu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.dewu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    # 'sign': '52900e556b258d9e26f9bbf74ee00b7e',
    'pickRuleId': 644450,
    'pageNum': 1,
    'pageSize': 24,
    'filterUnbid': True,
    'showCspu': True,
}

with open("./getsign.js") as fp:
    jscode = fp.read()

sign = execjs.compile(jscode).call('getSign', json_data)
print(sign)
json_data['sign'] = sign

session = requests.Session()
response = requests.post(
    'https://app.dewu.com/api/v1/h5/commodity-pick-interfaces/pc/pick-rule-result/feeds/info',
    cookies=cookies,
    headers=headers,
    data=json.dumps(json_data),
)

print(response.json())
