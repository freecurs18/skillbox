gradusy = int(input('Темература на улице: '))
beg = 0
while gradusy > 15:
    beg += 20
    gradusy -= 2
    beg += 10
print(beg)