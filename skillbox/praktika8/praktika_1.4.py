lower = int(input("Введите нижнюю границу диапазона:"))
upper = int(input("Введите верхнюю границу диапазона:"))
n = int(input("Введите делитель:"))
count = 0
summ = 0
for i in range(lower, upper + 1):
    if(i % n == 0):
        summ += i
        count += 1
arifmet = summ/count
print('Среднее арифметическое всех чисел отрезка:',arifmet)