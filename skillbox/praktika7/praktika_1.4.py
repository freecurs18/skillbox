count = 0
for i in range(30, 36):
    print ('Людей в',i,'секторе: ',end=''); people = int(input())
    if people < 10:
        print("Всё спокойно.")
    else:
        count += 1
        print("Нарушение! Слишком много людей в секторе!")
print("Количество нарушений:", count)

