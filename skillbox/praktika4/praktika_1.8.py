hours = int(input('Введите количество часов отработанных в этом месяце: '))
kredits = int(input('Введите остаток по кредиту: '))
food = int(input('Введите затраты на еду: '))
rest_time = (((200*hours)/2**3)+hours)
all_money = kredits + food
expenses = rest_time - all_money
print('=============')
print('Зарплата', rest_time)
print('Траты', all_money)

if rest_time <= expenses:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придёться работать!')