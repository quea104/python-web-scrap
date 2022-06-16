import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

# 웹 드라이버 시동 - 창이 없는 크롬(Headless Chrome)
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get('https://accounts.google.com/')
wait = WebDriverWait(driver, timeout=2)
time.sleep(2)

driver.find_element(by=By.CSS_SELECTOR, value='#identifierId').send_keys('ds.seo@itnbasic.com', Keys.ENTER)
time.sleep(2)

login_action = ActionChains(driver).send_keys('itnbasic12#$').key_down(Keys.ENTER).perform()
# ActionChains 에 대한 정보가 다음에 남아 있지 않도록 reset
# login_action.reset_actions()
time.sleep(2)

driver.get('https://mail.google.com/mail/u/0/?ogbl#inbox')
time.sleep(2)

driver.find_element(by=By.XPATH, value='/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div').click()

email_action = ActionChains(driver).send_keys('ds.seo@itnbasic.com').key_down(Keys.TAB).key_down(Keys.TAB).pause(0.5)\
    .send_keys('TEST!!!').key_down(Keys.TAB)\
    .send_keys('TEST TEXT OK!!!!!!!!!!!').key_down(Keys.TAB).pause(1).key_down(Keys.ENTER)\
    .perform()
# email_action.reset_actions()

time.sleep(2)
# 인박스에 메일을 스크래핑 하기 위해 페이지 소스 가져오기
html = driver.page_source

# 종료
driver.close()

# 파싱을 위해 BeautifulSoup 객체 만들기
soup = BeautifulSoup(html, 'lxml')

# select가 안될 경우 find 사용하기
tags = soup.find_all('table')

print(tags)
