import requests
import pandas as pd

headers = {
    'Authorization': 'KakaoAK e3af16b6ad94084e7ba41b69f93103ea',
}
parameters = {
    'query': '지브리'
}

res = requests.get('https://dapi.kakao.com/v2/search/blog', headers=headers, params=parameters)

result_documents = []
for document in res.json().get('documents'):
    result_documents.append(
        [
            document.get('blogname'),
            document.get('contents'),
            document.get('datetime'),
            document.get('thumbnail'),
        ]
    )

df = pd.DataFrame(result_documents)
df.to_excel('kakao_result.xlsx')

print(res.json())
