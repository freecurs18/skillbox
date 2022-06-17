print('Если ваша покупка будет больше 10000 руб., то магазин предостовляет скидку в 10%')
coast1 = int(input('Введите стоймость первого товара: '))
coast2 = int(input('Введите стоймость второго товара: '))
coast3 = int(input('Введите стоймость третьего товара: '))
sum_coast = coast1 + coast2 + coast3
discount = sum_coast * (10 / 100)
print('===================')
if sum_coast > 10000:
    sum_coast = sum_coast - discount
print('Ваша итоговая сумма',sum_coast,'руб.')
print('Ваша скидка составила',discount)