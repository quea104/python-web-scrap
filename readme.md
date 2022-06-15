#22.06.14~16

---
- 웹 크롤링
    - 인터넷의 데이터(HTML, 이미지, 동엿아, 음성)을 기계적으로 수집하는 행위

- 웹 스크래핑
    - 웹 페이지의 HTML을 가져와서 원하는 정보를 뽑아(extract) 내는 것

    - 합법적인가?
        - 저작권 위반, 업무방해죄

    - 절차
        1. 사전작업: 웹 페이지 분석
           - HTTP 포함 웹 기초
        2. HTML 전체 가져오기
           - request : HTTP 클라이언트 라이브러리 사용, 최초로 응답 준 정보만 사용 가능.
           - 터미널에서 requests 패키지 설치
           - 예시
           ```
           import requests
           
           res = requests.get('https://finance.naver.com/')
           ```
           - 만약 호출시 Response [406] 에러(unauthorized error)가 발생하면 웹 스크래핑을 차단한 페이지임.
        3. 가져온 HTML에서 데이터 추출 - parser
           - beautifulsoup: 파이썬 대표 HTML parser (for web scraping), 오픈소스
           - 터미널에서 beautifulsoup 패키지 설치           
           - CSS seelector 활용
             > chrome > F12(검사) > 해당 element > 오른쪽 마우스 클릭 > copy > copy selector
           - selector 예
             > #content > div > section > div > div > ul > li:nth-child(1) > h3 > a
           - 예시
             ```
             import requests
             from bs4 import BeautifulSoup
             
             res = requests.get('https://finance.naver.com/')
             
             soup = BeautifulSoup(res.text, 'html.parser')
             element = soup.select_one('#content > div > section > div > div > ul > li:nth-child(1) > h3 > a')
             
             print(element.text)
             ```
        4. 가져온 데이터를 파일로 저장
           - pandas : 데이터 분석 툴 라이브러리, 가장 많이 사용, dataframe 다룸.
           - 터미널에서 pandas 패키지 설치
           - 예시
             ```
             import requests             
             from bs4 import BeautifulSoup
             # coding conventions => 많이 사용해서 별칭을 사용
             import pandas as pd
             
             res = requests.get('https://finance.naver.com/')
             
             soup = BeautifulSoup(res.text, 'html.parser')
             element = soup.select_one('#content > div > section > div > div > ul > li:nth-child(1) > h3 > a')
             
             df = pd.DataFrame(element.text)
             df.to_excel('python-event.xlsx')
             ```
        5. 사람 처럼 읽기
         - HTTP > Request Headers > my user agent 이용
         - 구글 브라우저에서 'my user agent' 검색
           > Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
           
- pip
  - 파이썬으로 작성된 패키지 소프트웨어를 설치 · 관리하는 패키지 관리 시스템
  - pip 버전
    > pip --version

- 웹 데이터 수집
  - 데이터 수집의 3단계
    1. 선정(대상선정)
       - 웹에서는 how 보다 where가 더 중요.
    2. 수집(대상 위치에서 원하는 데이터 수집)
    3. 정리
       - 데이터 형태: 타뷸러 데이터, 2차원 행렬(백터) 데이터.
       - python에서 데이터 형태: 이중 리스트로 표현.
       - 데이터를 pandas를 사용하여 엑셀로 저장
  

- 터미널에서 패키지 설치
  1. requests : HTTP library
     > pip install requests
  2. beautifulsoup : Screen-scraping library
     > pip install beautifulsoup4
  3. openpyxl: Python library to read/write Excel 2010 xlsx/xlsm files
     > pip install openpyxl
  4. pandas : powerful Python data analysis toolkit
     > pip install pandas
  5. lxml : Powerful and Pythonic XML processing library, parsing 속도가 빠름
     > pip install lxml
 

- 설치 오류
  - 오류: pip install --upgrade pip 하고 나서 pip, python 명령어를 터미널에서 인식을 못함
  - 원인
    - pip를 업그레이드하려면 삭제 후 새버전을 설치하게 되는데 삭제 후 재설치가 정상적으로 되지 않은 것
    - 윈도우 터미널(cmd.exe)를 관리자 권한으로 실행하지 않은 상태에서 pip를 업그레이드하려고 하면 삭제는 문제없이 잘 되는데, 설치 시 권한 문제로 실패하면서 pip가 삭제된 상태로 남아 이런 현상이 자주 생기는 것으로 보인다.
    - https://devlog.jwgo.kr/2020/02/29/broken-pip-error/
    > ModuleNotFoundError: No module named ‘pip’
  - 해결
    - pip를 재설치
    ```
     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
     python get-pip.py
    ```

- 추가 설명
  - pandas 라이브러리
    - 개발자 Wes McKinney 개발
    - AQR Capital Management에서 재무 데이터에 대한 정량적 분석을 수행 하기 위한 고성능의 유연한 도구가 필요 하여 2008년에 판다 작업을 시작.
    - AQR을 떠나기 전에 그는 경영진에게 라이브러리를 오픈 소스로 허용하도록 설득.
  - 인터넷 세계 구조
    - surface web
      - 로그인 하지 않아도 접근 가능한 웹 페이지.
      - 구글, 네이버로 검색 가능.
      - 전체 인터넷의 4~5% 추정.
    - deep web
      - 일반적인 검색 엔진으로는 드러나지 않는, 표층 웹(surface web)에 속하지 않는 월드 와이드 웹 컨텐츠.
      - 로그인 해야만 접근 가능한 웹 페이지이나 소유주가 웹크롤러가 인덱싱하지 못하도록 차단한 웹 컨텐츠.
      - 전체 인터넷의 96~99% 추정.
      - clear web 이라고 부르는 표준 웹 브라우저를 통해 접근 가능.
    - dark web
      - 의도적으로 숨거진 deep web의 하위 집단.
      - 접속하기 위해서는 특정 브라우저가 필요.
      - 영국 대학교 연구권의 조사에 의하면 2015년 2천여개의 dark web 사이트의 컨텐츠 중 57%가 불법 컨텐츠였음.
      - 전체 인터넷의 5% 추정.
  - coding conventions
    - 코딩 규칙을 해당 언어로 작성된 프로그램의 각 측면에 대한 프로그래밍 스타일, 실습 및 방법을 권장하는 특정 프로그래밍 언어에 대한 일련의 지침
  - verbose code
    - one that needs more words, or longer words, than is necessary to adequately express the intent of the code.
    - there are many very long symbols or symbols.
  - programming paradigm
    - Imperative Programming
      - 명령형 프로그래밍(How)
      - 문제를 어떻게 해결해야 하는지 컴퓨터에게 명령을 내리는 방법의 프로그래밍
      - 알고리즘을 명시하고 목표는 명시하지 않는다.
        ```
        let a = [1, 2, 3, 4, 5];
        for(let i = 0; i < 5; i += 1) { 
          if(a[i] % 2 === ) {
            console.log(a[i]);
          }
        }
        ```
    - Declarative Prograaming
      - 절차적 프로그래밍(What)
      - 알고리즘을 명시 하지않고 목표만 명시한다.
        ```
        let a = [1, 2, 3, 4, 5];
        for(let i = 0; i < 5; i += 1) { 
          if(a[i] % 2 === ) {
            console.log(a[i]);
          }
        }
        ```

---