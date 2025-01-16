# -*- coding: utf-8 -*-
"""
@Name:        tmp_ex2.py
@Describe:    XXX
@Time:        2025/01/12 08:48:20
@Author:      Ray
@Version:     1.0
"""
import requests
from bs4 import BeautifulSoup
import logging


def fetch_page(url):
    """获取页面内容"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        response.encoding = 'utf-8'
        return response.text
    except requests.RequestException as e:
        logging.error(f"请求失败：{e}")
        return None


def parse_html(html, CLASS_NAME):
    """解析HTML并提取文章标题"""
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    ul_list = soup.find('ul', class_=CLASS_NAME)
    if ul_list:
        li_elements = ul_list.find_all('li')
        return [li.find('a').get_text(strip=True) for li in li_elements if li.find('a')]
    else:
        logging.warning("未找到指定的ul标签")
        return []


def save_to_file(data, filename):
    """将数据保存到文件"""
    with open(filename, 'w', encoding='utf-8') as file:
        count = 0
        for text in data:
            count += 1
            file.write("NO:"+str(count) + " " + text + '\n')


def main():
    URL = 'http://yuanchuang.caijing.com.cn/'
    CLASS_NAME = 'list'
    OUTPUT_FILE = './luffy_basic/outputs/output.txt'
    html = fetch_page(URL)
    if html:
        titles = parse_html(html, CLASS_NAME)
        save_to_file(titles, OUTPUT_FILE)
        logging.info(f"已保存 {len(titles)} 条数据到 {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
