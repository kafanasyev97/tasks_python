import random
first_team = [round(random.uniform(5, 10), 2) for x in range(20)]
second_team = [round(random.uniform(5, 10), 2) for x in range(20)]

winners = [(first_team[i_num] if first_team[i_num] > second_team[i_num]
else second_team[i_num]) for i_num in range(20)]

print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', winners)
