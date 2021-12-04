import requests

url = "https://imdb8.p.rapidapi.com/title/find"

querystring = {"q": "game of thr"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "4b3d784309msh1a54be2ab333712p1f580cjsn967b22d81802"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = response.json()

for line in json_response['results']:
    print(line)