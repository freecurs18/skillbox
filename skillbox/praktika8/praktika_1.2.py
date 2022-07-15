debtor = int(input('Введите количество должников: '))
count = 0
for i in range(0 , debtor + 1 , 5):
    print('Должник с номером: ', i)
    dolg = int(input('Сколько должны? '))
    count += dolg
print('Общая сумма долга:', count, 'рублей')