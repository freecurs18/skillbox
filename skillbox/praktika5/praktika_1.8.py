square = int(input('Введите площадь квартиры: '))
price = int(input('Введите стоймость квартиры: '))
if (square >= 100 and price <= 10) or (square >= 80 and price <= 7):
    print('Квартира подходит')
else:
    print('Квартира не подходит')