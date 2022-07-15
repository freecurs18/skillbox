positive_count = 0
negative_count = 0
estimation = 0
while -101 != estimation != 101:
    estimation = int(input('Введите оценку приложения от -100 до 100: '))
    if estimation == 0:
        break
    if estimation > 0 and estimation < 101:
        positive_count+= 1
    if estimation < 0 and estimation > -101:
        negative_count+= 1
    if -101 < estimation > 101:
        print('Вы ввели недопустимое значение')
        break
print('Положительных оценок:', positive_count)
print('Отрицательных оценок:', negative_count)