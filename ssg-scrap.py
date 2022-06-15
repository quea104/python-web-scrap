import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}
res = requests.get('https://www.coupang.com/np/search?component=&q=%EC%83%9D%EC%88%98&channel=user', headers=headers)
print(res)

soup = BeautifulSoup(res.text, 'html.parser')

a_item = [
    soup.select_one('#\35 625704601 > a > dl > dd > div > div.name').text,
    soup.select_one('#\35 625704601 > a > dl > dd > div > div.price-area > div > div.price > em > strong').text,
    soup.select_one('#\35 625704601 > a > dl > dd > div > div.price-area > div > div.price > span').text,
    soup.select_one('#\35 625704601 > a > dl > dd > div > div.price-area > div > div.delivery > span > em:nth-child(1)').text,
]

pd.DataFrame(a_item).to_excel('coupang.xlsx')

print('OK')