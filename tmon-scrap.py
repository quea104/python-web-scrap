import requests
from bs4 import BeautifulSoup
import pandas as pd

res = requests.get('https://www.ssg.com/service/bestMain.ssg?zoneId=5000016022')

soup = BeautifulSoup(res.text, 'lxml')

li_list = soup.select('#bestCategoryItem > li');

item_list = []

for li in li_list:
    item_list.append([
        int(li.select_one('div.cunit_prod > div.prod_top > span.tx_best').text),
        li.select_one('div.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko').text,
        int(li.select_one('div.cunit_info > div.cunit_price > div > em').text.replace(',', '')),
        'https://'+li.select_one('div.cunit_prod > div.thmb > a > img')['src'],
    ])

pd.DataFrame(item_list).to_excel('ssg.xlsx', header=['순위', '상품명', '가격', '사진'], index=False)

print('OK')