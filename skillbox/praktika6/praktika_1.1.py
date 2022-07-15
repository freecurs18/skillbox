number = 0
degree = 0
user = int(input('Введите число что бы его возвести в третью степень: '))
while number < user:
    number += 1
    degree = number ** 3
    print(number,'в степени 3 =',degree)