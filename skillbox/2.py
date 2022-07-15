count = 0
for a in(345,19,87,1020,421):
    print(a)
    if a >= 100 and a <1000 and a % 5 == 0:
        count += 1
        print(a,'Число выйгрышное')
print('Число победителей:', count)