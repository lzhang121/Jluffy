import time

import requests
import execjs

cookies = {
    'Hm_lvt_cadcf695428f7859d9d5e5d7bd270572': '1745034804',
    'HMACCOUNT': '9D91F8988AFF7E81',
    'SHOW_ACTIVITY_PANEL': 'false',
    'Hm_lpvt_cadcf695428f7859d9d5e5d7bd270572': '1745039836',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.fnscore.cn/score.html',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'Hm_lvt_cadcf695428f7859d9d5e5d7bd270572=1745034804; HMACCOUNT=9D91F8988AFF7E81; SHOW_ACTIVITY_PANEL=false; Hm_lpvt_cadcf695428f7859d9d5e5d7bd270572=1745039836',
}
timestamp = int(time.time() * 1000)
params = {
    'gameType': '1',
    'date': '2025-04-10',
    'hot': 'false',
    'onlyAnchor': 'false',
    'token': '',
    'timestamp': timestamp,

}
a= execjs.compile(open("fengniao.js").read())

sign = a.call("get_sign",timestamp)
params["sign"] = sign
response = requests.get('https://www.fnscore.cn/api/score/getListByDate', params=params, cookies=cookies,
                        headers=headers)

print(response.text)
