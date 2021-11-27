import json
import requests

url = 'https://api.coinbase.com/v2/exchange-rates'
response = requests.get(url)
rates = json.loads(response.text)

amount = 1145
print(amount * float(rates['data']['rates']['CHF']))

for code, value in rates['data']['rates'].items():
    print(f'1 $ is {code} {value}')
