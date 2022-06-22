hour = int(input("Введите время: "))
if (hour >= 8 and hour <= 22) and not (hour <= 15 and hour >= 14) and not (hour >=18 and hour <=20):
    print("Можно получить посылку")
else:
    print("Посылку получить нельзя")