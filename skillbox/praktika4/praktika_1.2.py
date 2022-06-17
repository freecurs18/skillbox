russian_lang = int(input('Введите баллы по русскому языку: '))
math = int(input('Введите баллы по математике: '))
informatics = int(input('Введите баллы по информатике: '))
summ_bally = russian_lang + math + informatics
if summ_bally == 270:
    print('Поздравляю! Ты поступил на бюджет!!!')
else:
    print('К сожелению, ты не прошел на бюджет')