one_side = int(input('Введите длину письма: '))
two_side = int(input('Введите высоту письма: '))
convert = 12
count = 0
while convert < one_side or convert < two_side:
    if convert < one_side:
        count += 1
        one_side = one_side / 2
        if convert < two_side:
            count += 1
            two_side = two_side / 2
print('Складывать ', count, 'раз')