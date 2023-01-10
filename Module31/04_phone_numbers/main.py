import re


text = ['9999999999', '999999-999', '99999x9999']
count = 1

for x in text:
    res = re.findall('[89]\d{9}', x)
    if res:
        print(count, 'номер: всё в порядке')
    else:
        print(count, 'номер: не подходит')
    count += 1
