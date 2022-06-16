import requests
from bs4 import BeautifulSoup


def download_image_from_url(url, name):
    res = requests.get(url)
    # res.content : 이미지 파일을 바이너리로 받아옴
    with open('./album-image/'+name, 'wb') as f:
        f.write(res.content)
    print(name + ' 저장 완료')


def main():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
    }

    # header 위변조
    res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)

    # html에서 데이터 추출
    soup = BeautifulSoup(res.text, 'html.parser')

    trs = soup.select('#lst50')

    # 타뷸러 데이터
    for tr in trs :
        img_url = tr.select_one('td:nth-child(4) > div > a > img')['src']
        img_name = img_url.split('/')[9]
        download_image_from_url(img_url, img_name)

    print('OK')


main()
