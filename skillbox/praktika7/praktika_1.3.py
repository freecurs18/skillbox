full_sallary = 0
months = 1
for months in range (1, 13):
    salary = int(input('Введите зарплату за месяц:'))
    full_sallary += salary
print('Средняя заплата за год:' , int(full_sallary / 12))