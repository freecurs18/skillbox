abiturient = int(input('Введите место в списке поступающих: '))
points = int(input('Введите количество баллов за экзамены: '))
if abiturient <= 10 and points >= 290:
    print('Поздравляем, вы поступили!')
    print('Бонусом вам будет начисляться стипендия.')
elif abiturient <= 10 and points < 290:
    print('Поздравляем, вы поступили!')
    print('Но вам не хватило баллов для стипендии.')
elif abiturient > 10:
    print('К сожалению, вы не поступили.')