import requests
import json

url_obiwan = json.loads(requests.get("https://swapi.dev/api/people/10/").text)
url_darthvader = json.loads(requests.get("https://swapi.dev/api/people/4/").text)

url_xwing = json.loads(requests.get("https://swapi.dev/api/starships/12/").text)
url_corusant = json.loads(requests.get("https://swapi.dev/api/planets/9/").text)

#URLs to pull data down from SWAPI