number = int(input('Введите число: '))
factorial = 1
for search in range(1, number + 1):
    factorial *= search
print('Факториал числа',number, 'равен', factorial)