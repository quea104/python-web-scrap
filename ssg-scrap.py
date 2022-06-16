import pprint

import requests
from bs4 import BeautifulSoup
import pandas as pd

res = requests.get('https://www.ssg.com/service/emart/dvstore/category.ssg?dispCtgId=6000095739')

soup = BeautifulSoup(res.text, 'lxml')

li_list = soup.select('#ty_thmb_view > ul > li')

products = []

for li in li_list:
    products.append([
            li.select_one('div.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko').text,
            int(li.select_one('div.cunit_info > div.cunit_price > div.opt_price > em').text.replace(',', '')),
            'https://' + li.select_one('div.cunit_prod > div.thmb > a > img.i1')['src'],
    ])

pprint.pprint(products)

pd.DataFrame(products).to_excel('ssg.xlsx', header=['상품명', '가격', '사진'], index=False)

print('OK')
