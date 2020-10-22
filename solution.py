lst = list(map(int, input().split()))
dct = [0] * 101

for number in lst:
    dct[number] += 1

line = ''
for i in range(101):
    line = ''.join((line, f'{i} ' * dct[i]))

print(line[:-1])
