count = 0
month = 0
while month >= 0:
    month = int(input('Введите число дней в месяце: '))
    if month == 0:
        break
    if month > 31:
        print('В месяце не может быть больше 31 одного дня')
        count-= 1
    if month%2 == 0:
        count += 1
print('Количество месяцев с четным количеством дней:',count)