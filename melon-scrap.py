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

# verbose code
rank = soup.select_one('#lst50 > td:nth-child(3) > div > span > span')
title = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
artist = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
album = soup.select_one('#lst50 > td:nth-child(7) > div > div > div > a')
song = [rank, title, artist, album]

# compact code - pythonic
a_song = [
    int(soup.select_one('#lst50 > td:nth-child(3) > div > span > span').text),
    soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text,
    soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text,
    soup.select_one('#lst50 > td:nth-child(7) > div > div > div > a').text,
]

pd.DataFrame(a_song).to_excel('melon.xlsx')

print('OK')