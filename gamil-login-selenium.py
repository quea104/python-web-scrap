import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# 브라우저 호출
driver = webdriver.Chrome('./chromedriver')

# 페이지 접속
driver.get('https://accounts.google.com/')
time.sleep(2)

# 아이디 입력
driver.find_element(by=By.CSS_SELECTOR, value='#identifierId').send_keys('ds.seo@itnbasic.com')
time.sleep(2)

# 다음 버튼 클릭
driver\
    .find_element(by=By.CSS_SELECTOR, value='#identifierNext > div > button')\
    .click()
time.sleep(2)

# 비밀번호 입력 후 엔터
driver.find_element(by=By.CSS_SELECTOR, value='#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys('itnbasic12#$', Keys.ENTER)

# 메모리 문제 때문에 꼭 닫아줘야 함
driver.close()
