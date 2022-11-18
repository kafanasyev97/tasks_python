players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
# asd = []
# for index, value in players.items():
#     index, value = list(index), list(value)
#     asd.append(tuple(index + value))
# print(asd)
# Сначала хотел сделать так, но потом узнал, что кортежи оказывается можно складывать между собой

result = [index + value for index, value in players.items()]
print(result)
