import requests as r

response = r.get('https://api.github.com/')
"""
1xx - подключение выполнено, но ответ не получен
2xx - успешное подключение к серверу 
3xx - перенаправление 
4xx - страница не найдена (404)
5xx - ошибка сервера 
"""
print(response)  # <Response 200>

