import requests as r

url = 'https://api.github.com/search/repositories'

try:
    response = r.get(url, params={'q': 'requests+language:cpp'})
    json_r = response.json()
    for repo in json_r['items']:
        print(repo['name'], repo['html_url'])
except:
    print('Oh-oh! Error occurred while processing!')

