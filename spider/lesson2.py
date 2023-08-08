#!/usr/bin/python
# coding: UTF-8

import requests
from bs4 import BeautifulSoup


def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    movie_list = []
    for i in range(0, 1):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
        r = requests.get(url, headers=headers, timeout=10)
        print(str(i + 1), "页响应状态码：", r.status_code)

        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            span_list = each.find_all('span', class_='title')
            print(span_list)

    return movie_list


movies_list = get_movies()
print(movies_list)
