profit = int(input('Введите ваш доход: '))
tax = 0
if profit >= 100000:
    tax = ((profit - 50000)*0.3) + ((50000 - 10000)*0.2) + 10000 * 0.13
elif profit >10000 and profit < 50000:
    tax = ((profit - 10000)*0.2) + 10000 * 0.13
elif profit <10000:
    tax = profit * 0.13
print('Ваш налог равен:',tax)