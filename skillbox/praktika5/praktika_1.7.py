one_number = int(input('Введите первое число: '))
two_number = int(input('Введите второе число: '))
three_number = int(input('Введите третье число: '))
if one_number == two_number == three_number:
    print('3. Все числа совпадают')
elif (one_number == two_number) or (one_number == three_number) or (two_number == three_number):
    print('2. Совпадают 2 числа')
else:
    print('0. Не совпадают ни одного числа')