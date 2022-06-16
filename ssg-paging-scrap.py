import pprint
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_li_list_from_url(products_url):
    res = requests.get(products_url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup.select('#ty_thmb_view > ul > li')


# PEP 8: E302 expected 2 blank lines
def main():
    products_total = []

    for page_num in range(1, 100):
        li_list = get_li_list_from_url(
            'https://www.ssg.com/service/emart/dvstore/category.ssg?dispCtgId=6000095740&page='+str(page_num)
        )

        if not li_list:
            print(str(page_num) + '페이지 종료')
            break

        print(str(page_num) + '페이지 스크래핑 중')
        products_page = []
        for li in li_list:
            # 리스트 끝에 x 1개 넣기
            products_page.append([
                li.select_one('div.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko').text,
                int(li.select_one('div.cunit_info > div.cunit_price > div.opt_price > em').text.replace(',', '')),
                'https:' + li.select_one('div.cunit_prod > div.thmb > a > img.i1')['src'],
            ])

        # 리스트 끝에 가장 바깥쪽 iterable의 모든 항목 넣기
        products_total.extend(products_page)

    #pprint.pprint(products_total)
    pd.DataFrame(products_total).to_excel('ssg.xlsx', header=['상품명', '가격', '사진'])
    print('OK')


main()
# PEP 8: W292 no newline at end of file
