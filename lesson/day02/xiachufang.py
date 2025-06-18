import requests
from urllib.parse import quote


# 编码
keyword = input('请输入菜品名称：')
encoded_keyword = quote(keyword)


url = "https://www.xiachufang.com/search/?keyword="+encoded_keyword+"&cat=1001"

payload = {}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.xiachufang.com/search/?keyword=%E9%A3%8E%E5%91%B3%E8%8C%84%E5%AD%90+&cat=1001',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'Cookie': 'bid=4oDWa0rH; __utma=177678124.70280027.1750229494.1750229494.1750229494.1; __utmc=177678124; __utmz=177678124.1750229494.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219781cea7c6b5b-0c1bbe9788a78e-18525636-1296000-19781cea7c7921%22%2C%22%24device_id%22%3A%2219781cea7c6b5b-0c1bbe9788a78e-18525636-1296000-19781cea7c7921%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_ecd4feb5c351cc02583045a5813b5142=1750229494; HMACCOUNT=5B7735EBB1CAB187; xcf_clearance=Y+A3PmG1kf3hfrz8mMON8hRrFZlUT6Ykdxh+VbON1JOJ5B/TKyDK0rH7x+JPx6yu7MN7HfV3KyK4ofQQ4DQjGgTB6IkI9EMSAs2QjLI59cTZvcVqCjcuuo/1/WRBj+8R6oujjQMu29pujtOsBsGAHFIAO2Gbq3cuwlQ/UhrKAWXsV4NGpY3rJ2QQ5eTYDOXT4VKAlKfUl7C25z+ohTFEyFxxaGw2mzF9Pd3QyLlfpsI=; tfstk=gWcoxm9A5os_6H-YHjNWQBqX6BJYN7NQRDCLvWEe3orf2gC-8wRnvDidee9SKMqmAue8aL1U80ZjvT3JFvqnVcc8wQt7t2usADL7aXDftVgIwUNpP7g7OW-9XChnP4NQ9qr24bfVuPu4z_zyHSWCdxhyXCdtzSHcbmxt9Jw3Mu4UTzyUTZ807ozz8Drz3izg5WPEYJP40y4a8a5z8-80RorUTWoUgE4L0k8zPZr-Y0G2DLSW_m2UWj4uElu2165HUzSTX4zCT6uar8XmzofFTjMvjkGgjIj4D2usL-cHN_FIkAmnLm8FTkD4Sc4t2I5uTxomsRuXj_Zo30G3wROh-rDiu0cutdb7kb0q1JcWqsrocqkTNf-ftcuxWbwjthj4AYU_gzDD8trzLgrV3OWtl6a2JjWCd8zbolhKMZP5eL7oeEYcQAwzlzR9oEXCy8zbolYDoO84UrayW; __utmb=177678124.11.10.1750229494; Hm_lpvt_ecd4feb5c351cc02583045a5813b5142=1750229770'
}

response = requests.request("GET", url, headers=headers, data=payload)

page_text = response.text

with open('xiaochufang.html', 'w') as fp:
    fp.write(page_text)
