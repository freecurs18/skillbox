one_kvartal = int(input('Введите доход первого квартала '))
two_kvartal = int(input('Введите доход второго квартала '))
three_kvartal = int(input('Введите доход третьего квартала '))
four_kvartal = int(input('Введите доход четвёртого квартала '))
first_six_monthe = one_kvartal + two_kvartal
second_six_monthe = three_kvartal + four_kvartal
razniza_megdu_kvartalavi = first_six_monthe / second_six_monthe
print ('=======================')
print ('Суммма первого и второго квартала' , first_six_monthe, 'руб')
print ('Суммма третьего и четвёртого квартала', second_six_monthe, 'руб')
print ('Отношение первого квартала ко второму',razniza_megdu_kvartalavi)