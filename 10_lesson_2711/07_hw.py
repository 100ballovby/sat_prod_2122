import json
import requests

url = 'https://api.github.com/users/GreatRaksin/repos'
response = requests.get(url)
repositories = json.loads(response.text)

for repo in repositories:
    print(repo['svn_url'])

"""
Найти все репозитории, основным языком которых является 
Python и вывести их в формате:

Name {name_of_repo}
Link {svn_url}
Clone url {clone_url}
Created at {created_at}

!!!!⭐️⭐️⭐️⭐️!!!!
Создать словарь, который содержит 
все данные из первого задания
"""


