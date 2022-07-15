print('Программа ищет потерянную карточку.')
totalCards = int(input('Введите количество карточек: '))
total_Sum = 0
remaining_Sum = 0
remeining_card = 0
for card in range(1, totalCards + 1):
    total_Sum += card
for card in range(totalCards - 1):
    remeining_card = int(input('Номер оставшейся карты'))
    remaining_Sum += remeining_card
summ = total_Sum - remaining_Sum
print('Номер потерявшейся карточки: ',summ)