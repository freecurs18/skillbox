x = int(input('Введите координату X: '))
y = 0
if x > 0:
    y = x - 12
    print(y)
elif x == 0:
    y = 5
    print(y)
elif x < 0:
    y = x**2
    print(y)
