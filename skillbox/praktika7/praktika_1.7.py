print('Программа читает среднее арифметическое Всех чисел отрезка [a:b]')
a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
summ = 0
count = 0
for i in range(a, b +1):
    if i % 3 == 0:
        count += 1
        summ += i
if count == 0:
    print('Расчет невозможен, так как нет подходящих чисел')
else:
    print('Среднее арифметическое:',summ / count)