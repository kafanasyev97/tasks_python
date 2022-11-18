import random

original_list = [random.randint(0, 10) for x in range(10)]
print('Оригинальный список:', original_list)
zip_list = list(zip(original_list[::2], original_list[1::2]))
print('Новый список:', zip_list)

# text = [random.randint(0, 10) for x in range(10)]
# print(text)
# text_1 = text[::2]
# text_2 = text[1::2]
# people = list(zip(text_1, text_2))
# print(people)

# s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# k1 = (s[0],s[1])
# k2 = (s[2],s[3])
# k3 = (s[4],s[5])
# k4 = (s[6],s[7])
# k5 = (s[8],s[9])
# print([k1,k2,k3,k4,k5])