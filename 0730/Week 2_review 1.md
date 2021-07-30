# Week 2_review 1

## 1. 평균점수구하기

표준 입력으로 국어, 영어, 수학,과학 점수가 입력되고 평균 점수를 출력한다.

``` 
입력값: 83 92 97 90
출력값:88
```

```python
a, b, c, d = map(int, input().split())

print((a+b+c+d)/4)
```



## 2. 크롤링1

agify에서 이름에 대한 나이를 크롤링 해보기

```python
import requests

url = 'https://api.agify.io?name=michael'

# 응답 jsonstr을 dict로 파싱해서 response에 저장
response = requests.get(url).json()

print(response['age'])
```



## 3. 크롤링2

네이버 금융에서 달러 환율을 크롤링해보기

```python
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'

response = requests.get(url)

data = BeautifulSoup(response.text, 'html.parser')

exchange_rate = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print(exchange_rate)
```



## 4. 크롤링3

tmdb에서 영화 제목으로 검색하고 id를 리턴하기

```python
import requests
from pprint import pprint


class TMDBHelper:

    def __init__(self, api_key = None):
        self.api_key =api_key

    def get_request_url(self, method = '/movie/popular', **kwargs):
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'
        return request_url


    # 제목으로 영화 검색 후, 검색결과에서 id를 return
    def get_movie_id(self, title):
        request_url = self.get_request_url('/serch/movie', query=title, region='KR', language='ko')
        data = requests.get(request_url).json()
        results = data.get('results')
        if results:
            movie_id =results[0]['id']
            return movie_id
        else:
            return None
```

