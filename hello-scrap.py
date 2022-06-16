# print('test')
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.python.org/events/')

# res.text : request의 body 가져오기
soup = BeautifulSoup(res.text, 'html.parser')

# list 반환
listElement = soup.select('#content > div > section > div > div')
# print(listElement)

# element 반환
element = soup.select_one('#content > div > section > div > div > ul > li:nth-child(1) > h3 > a')
print(element.text)


res_n = requests.get('https://finance.naver.com/')

soup_n = BeautifulSoup(res_n.text, 'html.parser')

# list 반환
listElement_n = soup_n.select('#_topItems1 > tr > th > a')
print(listElement_n)

