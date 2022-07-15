num = int(input('Введите число и программа определит сколько в нём цифр: '))
count = 0
while num != 0:
    count += 1
    lust_num = num % 10
    num //= 10
print('В этом числе ',count, 'цифр')