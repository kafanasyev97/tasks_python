import requests
import json


my_req = requests.get('https://swapi.dev/api/starships/10/')
res = json.loads(my_req.text)
ssd = {}
ssd['name'] = res['name']
ssd['max_atmosphering_speed'] = res['max_atmosphering_speed']
ssd['starship_class'] = res['starship_class']

dop_lst = []

for elem in res['pilots']:
    dop_dict = {}
    pilot = requests.get(elem)
    i_pilot = json.loads(pilot.text)
    gg = requests.get(i_pilot['homeworld'])
    result = json.loads(gg.text)
    dop_dict['name'] = i_pilot['name']
    dop_dict['height'] = i_pilot['height']
    dop_dict['mass'] = i_pilot['mass']
    dop_dict['homeworld'] = result['name']
    dop_dict['homeworld_url'] = i_pilot['homeworld']
    dop_lst.append(dop_dict)

ssd['pilots'] = dop_lst
print(json.dumps(ssd, indent=4))


with open('info.json', 'a') as file:
    json.dump(ssd, file, indent=4)
