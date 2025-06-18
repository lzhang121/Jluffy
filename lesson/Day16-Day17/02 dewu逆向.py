import requests
import execjs

cookies = {
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219670dfd0471e73-0b358487b0c6e68-1a525636-2073600-19670dfd048680%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2NzBkZmQwNDcxZTczLTBiMzU4NDg3YjBjNmU2OC0xYTUyNTYzNi0yMDczNjAwLTE5NjcwZGZkMDQ4NjgwIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219670dfd0471e73-0b358487b0c6e68-1a525636-2073600-19670dfd048680%22%7D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.dewu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.dewu.com/',
    'SK': '',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'ltk': 'D8OBwovCo8KXF8KLw4nCkMKDL8KXwpTCpMOTBcOmwpbCncKnMTnCl3zDncOjU8K7KX3Dg3fCqVnDgcOAw54edMKUPxnDnMO0wqDCi8O4wovCoMOO',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sessionid': 'wfl3c1mb-p2f5-au2m-rou6-lwf5jljuh6rc5olp',
    'shumeiId': '2025042614535899c164e2243d76a14696b5046bb3184d00c097f17a3addba',
    'traceparent': '00-f5a5d5ff680c86a1dd202342715acbd5-b2c28c781e24e5ef-01',
    # 'Cookie': 'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219670dfd0471e73-0b358487b0c6e68-1a525636-2073600-19670dfd048680%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2NzBkZmQwNDcxZTczLTBiMzU4NDg3YjBjNmU2OC0xYTUyNTYzNi0yMDczNjAwLTE5NjcwZGZkMDQ4NjgwIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219670dfd0471e73-0b358487b0c6e68-1a525636-2073600-19670dfd048680%22%7D',
}

json_data = {
    'pickRuleId': 644479,
    'pageNum': 10,
    'pageSize': 24,
    'filterUnbid': True,
    'showCspu': True,
}

sign = execjs.compile(open("03 dewu.js").read()).call("c", json_data)
print("sign:::", sign)

json_data["sign"] = sign
response = requests.post(
    'https://app.dewu.com/api/v1/h5/commodity-pick-interfaces/pc/pick-rule-result/feeds/info',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)
