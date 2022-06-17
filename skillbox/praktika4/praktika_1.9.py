car_mileage = int(input('Введите трёхзначное число пробега: '))
current_day = int(input('Введите текущий день от 1 до 31: '))
b = int(car_mileage//100)
c = int(car_mileage%100//10)
d = int(car_mileage%10//1)
mileage = b+c+d
print('================')
print('Сумма всех трёх чисел пробега:',mileage)
print('Сегодняшнее число:',current_day)
if mileage > current_day:
    print('Сброс')
    print('Пробег: 0')
else:
    print('Сегодня не сломался')
    print('Пробег:', car_mileage)
