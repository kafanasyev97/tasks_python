import re


text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

car = re.findall(r'\b\w\d{3}\w{2}\d{2,3}', text)
print('Список номеров частных автомобилей:', car)

taxi = re.findall(r'\b\w{2}\d{3}\d{2,3}', text)
print('Список номеров частных автомобилей:', taxi)

