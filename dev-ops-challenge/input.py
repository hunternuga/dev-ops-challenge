from time import sleep
from url import *
import yaml

with open('input.yaml') as s:
    try:
        data = yaml.safe_load(s)
    except yaml.YAMLError as exc:
        print(exc)
    ##Loading input from Yaml file.

def get_film_name(film_url):
    f = requests.get(film_url)
    film = json.loads(f.text)
    name = film['title']
    return name
    #Grabbing film title - function
def get_starship_name(starship_url):
    s = requests.get(starship_url)
    starship = json.loads(s.text)
    name_s = starship['name']
    return name_s
    #Grabbing starship name - function
def get_resident_name(resident_url):
    r = requests.get(resident_url)
    residents = json.loads(r.text)
    name_r = residents['name']
    return name_r
    #Grabbing resident name - function

f = open("swapi-output.json", "w+")
    #Creating output.json file

for name in data['results']:
    while True:
        film_results = []
        ship_results = []
        resident_results = []
        if name['id'] == 10:
            name['name'] = url_obiwan['name']
            name['gender'] = url_obiwan['gender']
            name['species'] = url_obiwan['species']
            name['url'] = url_obiwan['url']
            for films in url_obiwan['films']:
                for nested_films in name['films']:
                        film_results.append(get_film_name(films))
                        nested_films['title'] = film_results
            for ships in url_obiwan['starships']:
                for nested_ships in name['starships']:
                    ship_results.append(get_starship_name(ships))
                    nested_ships['name'] = ship_results
        if name['id'] == 4:
            name['name'] = url_darthvader['name']
            name['gender'] = url_darthvader['gender']
            name['species'] = url_darthvader['species']
            name['url'] = url_darthvader['url']
            for films in url_darthvader['films']:
                for nested_films in name['films']:
                    film_results.append(get_film_name(films))
                    nested_films['title'] = film_results
            for ships in url_darthvader['starships']:
                for nested_ships in name['starships']:
                    ship_results.append(get_starship_name(ships))
                    nested_ships['name'] = ship_results
        if name['id'] == 9:
            name['name'] = url_corusant['name']
            name['climate'] = url_corusant['climate']
            name['terrain'] = url_corusant['terrain']
            name['url'] = url_corusant['url']
            for residents in url_corusant['residents']:
                for nested_residents in name['residents']:
                    resident_results.append(get_resident_name(residents))
                    nested_residents['name'] = resident_results
        if name['id'] == 12:
            name['name'] = url_xwing['name']
            name['max_atmosphering_speed'] = url_xwing['max_atmosphering_speed']
            name['manufacturer'] = url_xwing['manufacturer']
            name['crew'] = url_xwing['crew']
            name['url'] = url_xwing['url']
    # Nested if statements pulling data and assigned values to YAML keys in input.yaml

f.write(json.dumps(data, indent=4))
print(f"Output has been written!")
time.sleep(30)
print(f'Open {output_file} to view data. Sleeping for 30 more seconds to view...')
time.sleep(30)
#Writing output and sleeping to pull data from 
