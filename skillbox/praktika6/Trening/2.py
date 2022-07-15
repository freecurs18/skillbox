new_car = int(input('Новая машина стоит 500000 '))
while new_car < 500000:
    zp = int(input('Новая машина стоит 500000, сколько доложишь? '))
    new_car += zp
    print(new_car)
print(new_car)