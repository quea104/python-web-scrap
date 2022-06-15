import pprint

import requests
from bs4 import BeautifulSoup
import pandas as pd

# dictionary, dict 타입 : key-value {}
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}

# header 위변조
res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)

# html에서 데이터 추출
soup = BeautifulSoup(res.text, 'html.parser')

trs = soup.select('#lst50')

song_list = []

# 타뷸러 데이터
for tr in trs :
    song_list.append([
        int(tr.select_one('td:nth-child(2) > div > span.rank').text),
        tr.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text,
        tr.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text,
        tr.select_one('td:nth-child(7) > div > div > div > a').text,
    ])

# pretty print
pprint.pprint(song_list)

pd.DataFrame(song_list).to_excel('melon_chart.xlsx', header=['순위', '제목', '가수', '앨범명'], index=False)

print('OK')