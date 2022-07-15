contribution = int(input('Введите сумму вклада: '))
deposit_percentage = int(input('Под какой процент вы положили: '))
expected_result = int(input('Какой должна быть окончательная сумма: '))
payback_period = 0
while contribution < expected_result:
    contribution*= 1 + deposit_percentage/100
    x = int(100 * contribution) / 100
    payback_period+= 1
print (payback_period)