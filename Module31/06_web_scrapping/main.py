import requests
from re import findall

response = requests.get('http://www.columbia.edu/~fdc/sample.html')
# Для любого сайта, я так полагаю, необходимо просто вместо ссылки поставить input('Вставьте ссылку: ')
result_beta = findall(r'>.+</h3>', response.text)
release = list(map(lambda x: x[1:-5], result_beta))
print(release)
