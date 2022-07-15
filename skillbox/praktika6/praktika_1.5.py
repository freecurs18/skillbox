happy_ticket = 0
while happy_ticket >= 0:
    happy_ticket = int(input('Введите 6-ти значный номер билета: '))
    a = (happy_ticket // 100000)
    b = (happy_ticket % 100000 // 10000)
    c = (happy_ticket % 10000 // 1000)
    d = (happy_ticket % 1000 // 100)
    e = (happy_ticket % 100 // 10)
    f = (happy_ticket % 10)
    right_side = a+b+c
    left_side = d+e+f
    print('Правая сторона: ',right_side)
    print('Левая сторона: ',left_side)
    if right_side == left_side:
        print('Билет счастливый')
    else:
        print('Не счастливый')