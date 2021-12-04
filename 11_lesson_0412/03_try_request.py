import requests as r
from requests.exceptions import HTTPError

urls = ['https://api.github.com/',
        'https://api.github.com/durak']

for url in urls:
    try:
        response = r.get(url)
        # когда запрос прошел, никаких ошибок не будет возникать
        response.raise_for_status()
        print(response.content)  # содержание ответа
        print(response.json())  # содержание ответа в JSON-формате
        print(response.headers)  # полезная информация об ответе
    except HTTPError as http_e:
        print(f'HTTP error occurred: {http_e}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(f'Successfully! Code: {response.status_code}')