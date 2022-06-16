import time
from selenium import webdriver
from bs4 import BeautifulSoup


# 웹 브라우저 호출 - chromedriver 경로를 지정하여 웹드라이버 객체 생성, private 모드로 실행
driver = webdriver.Chrome('./chromedriver')

# url 접근
driver.get('https://www.coupang.com/np/campaigns/82/components/194176')

# 로딩 된 후에 기다리기 - 사람이 행동하는 것처럼 보여주기 위해
#time.sleep(2)

# source get
html = driver.page_source

# 데이터 정제
soup = BeautifulSoup(html, 'lxml')

tags = soup.select('#productList > li')

print(tags)

# 메모리 문제 때문에 꼭 닫아줘야 함
driver.close()
