number = int(input())

for i in range(1, number + 1):
    for j in range(i):
        print('*', end="")
    print()
for h in range(number - 1, 0, -1):
    for k in range(h):
        print('*', end='')
    print()