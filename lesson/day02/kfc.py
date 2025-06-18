import requests
from urllib.parse import quote

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

address = "北京"
encoded_address = quote(address)

payload = "cname=" + encoded_address + "&pid=&keyword=TO&pageIndex=1&pageSize=10"
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.kfc.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'route-cell=ksa; ASP.NET_SessionId=zpu4tobygcngcoamd4kxx105; VOLCALB=fdd0f4400fd280c32c1111dc47526f54|1750230697|1750229515; VOLCALB=fdd0f4400fd280c32c1111dc47526f54|1750230730|1750229515; VOLCALBCORS=fdd0f4400fd280c32c1111dc47526f54|1750230730|1750229515; route-cell=ksa'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
