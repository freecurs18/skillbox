name = str(input('Введите имя должника: '))
debt = int(input('Введите сумму долга должника: '))
print (name,'ваша задолжность составляет',debt,'рублей')
while debt !=0:
    dolg = int(input('Сколько рублей вы внесёте прямо сейчас что бы погасить долг: '))
    if dolg != debt:
        print('Маловато!',name,'Давайте еще раз.')
    elif dolg >= debt:
        print('Отлично!',name,'Вы погасили долг. Спасибо!')
        break