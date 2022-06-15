import requests
from bs4 import BeautifulSoup
# coding conventions => 많이 사용해서 별칭을 사용
import pandas as pd

# 1. 해당 URL을 통해 HTML 전달 받기
res = requests.get('https://www.python.org/events/')

# 2. 응답이 정상적인 것이 확인되면 BeautilfulSoup
soup = BeautifulSoup(res.text, 'html.parser')

# 3. 실제 컨텐츠 확보
# 이벤트 날짜
event_date = soup.select_one('#content > div > section > div > div > ul > li:nth-child(1) > p > time').text
# 이벤트 명
event_name = soup.select_one('#content > div > section > div > div > ul > li:nth-child(1) > h3 > a').text
# 이벤크 종류
event_type = soup.select_one('#content > div > section > div > div > ul > li:nth-child(1) > p > span').text
# list화
a_event = [event_type, event_name, event_type]

# 4. list 를 엑셀로 변환 --> pandas 라이브러리 사용
df = pd.DataFrame(a_event)
df.to_excel('python-event.xlsx')
print('Save Excel file well')



