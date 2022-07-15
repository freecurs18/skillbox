riddle = int(input('Загадали число: ' ))
point = 0
while True:
  point += 1
  attempt = int(input('Число от 1 до 20 '))
  if attempt < riddle:
    print('Число меньше чем нужно. Попробуйте еще раз! ')
  if attempt > riddle:
    print('Число больше чем нужно. Попробуйте еще раз! ')
  if attempt == riddle:
    print(riddle, 'Вы угадали! Число попыток: ', point)
    break