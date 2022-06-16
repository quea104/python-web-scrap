import requests

res = requests.get('https://dog.ceo/api/breed/hound/images')

# api 는 json 또는 xml 형태로 데이터 전송
# 리스트 [] 로 데이터 받기
dogs = res.json().get('message')

print(dogs)