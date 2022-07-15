money = 0
count = 0
for i in range(1, 11):
    print('Введите сумму вашей зарплаты за', i, 'месяц: ', end=''); money1 = int(input())
    if money > money1:
        count += 1
    money = money1

if count > 0:
    print('Зарплата возрастает не упорядоченно...')
else:
    print('Зарплата возрастает упорядоченно...')