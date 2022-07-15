task = 0
time = 0
print('Начался 8ми часовой рабочий день')
while time != 8:
    maxim = int(input('Сколько задач решит Максим: '))
    task+= maxim
    time+= 1
    print(time,'-й час')
    wife = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет):'))
print('Рабочий день закончился. Всего выполнено задач:',task)
if wife == 0:
    print('Нужно зайти в магазин.')

