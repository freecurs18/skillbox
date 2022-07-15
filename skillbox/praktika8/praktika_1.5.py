one_segment = int(input('Введите первую часть отрезка: '))
two_segment = int(input('Введите вторую часть отрезка: '))
step = int(input('Введите шаг: '))
for i in range(two_segment, one_segment - 1, step):
    y = (i**3) + (2*i**2) - (4*i) + 1
    print('В точке',i,'функция равна',y)