violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
total_time = 0
count_songs = int(input('Сколько песен выбрать? '))
for i_el in range(count_songs):
    name_song = input(f'Название {i_el + 1} песни: ')
    for i in range(len(violator_songs)):
        if violator_songs[i][0] == name_song:
            total_time += violator_songs[i][1]

print(f'Общее время звучания песен: {round(total_time, 2)} минуты')