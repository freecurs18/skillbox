Kostya = int(input('У Константина выпало число: '))
Vladelec = int(input('У владельца выпало число: '))
if Kostya >= Vladelec:
    print('Разница между Костей и владельцем',Kostya - Vladelec, 'очко(ов)')
    print('Костя платит!')
else:
    print('Владелец платит')
print('Игра окончена!')