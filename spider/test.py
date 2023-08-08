#!/usr/bin/python
# coding: UTF-8

import requests
from bs4 import BeautifulSoup

url = 'http://www.santostang.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
title = soup.find('h1', class_="post-title").a.text.strip()
print(title)

with open('test.txt', "a+") as f:
    f.write(title)
    f.close()