import requests
import time
import execjs

headers = {
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://www.fnscore.cn/score.html',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
}

now = str(int(time.time() * 1000))
params = {
    'gameType': '5',
    'date': '2025-04-26',
    'hot': 'false',
    'onlyAnchor': 'false',
    'token': '',
    'timestamp': now,

}
p = f"timestamp={now}&secret=KHVheWluZ18zZWNyZXRfYXBB"
sign = execjs.compile(open("./08_fengniao.js").read()).call("get_sign", p)
params["sign"] = sign

response = requests.get('https://www.fnscore.cn/api/score/getListByDate', params=params, headers=headers)

print(
    response.text
)
