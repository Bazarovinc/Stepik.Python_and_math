"""Функция, принимающая колличество пончиков, и возвращающая строку:
'Всего пончиков: <число>', если пончиков не больше 9
'Всего пончиков: много', если пончиков больше 9"""


def donuts(n):
    if n <= 9:
        count = n
    else:
        count = 'много'
    return "Всего пончиков: {}".format(count)


def donuts_1(n):
    count = n if n <= 9 else 'много'
    return "Всего пончиков: {}".format(count)


print(donuts(7))
print(donuts_1(7))
