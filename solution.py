import re

s = 'Имя: Борис. День рождения: 15 апреля 1972г.'
regex = r'Имя: ([а-яА-Я]+). День рождения: (\d+) ([а-яА-Я]+) (\d+)г?.?'
match = re.search(regex, s)
if match is not None:
    print(f'Имя: {match.group(1)}')
    print(f'Месяц рождения: {match.group(3)}')
else:
    print('Формат строки не совпадает')

'''
--------------------------------



--------------------------------



--------------------------------

imax = 0
jmax = 0
# j0 = -1
# j1 = -1
# j2 = -1
i0 = 0
i1 = -1
i2 = -1

n = int(input())
a = list(map(int, input().split()))
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]
print(*p)

for j in range(1, n + 1):
    # print(p[j], imin0, imin1, imin2, ibest, jbest, p[jbest] - p[ibest])

    if p[j] % 3 == 0 and j - 0 > jmax - imax:
        jmax = j
        imax = 0
    elif p[j] % 3 == 1:
        if i1 == -1:
            i1 = j
        elif j - i1 > jmax - imax:
            jmax = j
            imax = i1
    else:
        if i2 == -1:
            i2 = j
        elif j - i2 > jmax - imax:
            jmax = j
            imax = i2

if jmax == 0:
    print(-1)
else:
    print(imax + 1, jmax)

--------------------------------

ibest = 0
jbest = 0
imin0 = 0
imin1 = 0
imin2 = 0

n = int(input())
a = list(map(int, input().split()))
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]
# print(*p)

for j in range(1, n + 1):
    # print(p[j], imin0, imin1, imin2, ibest, jbest, p[jbest] - p[ibest])

    if p[j] % 3 == 0:
        if (p[j] - p[imin0]) % 3 == 0 and p[j] - p[imin0] > p[jbest] - p[ibest]:
            jbest = j
            ibest = imin0
        elif ibest == 0 and jbest == 0:
            jbest = j
        if p[j] < p[imin0]:
            imin0 = j
    elif p[j] % 3 == 1:
        if (p[j] - p[imin1]) % 3 == 0 and p[j] - p[imin1] > p[jbest] - p[ibest]:
            jbest = j
            ibest = imin1
        elif p[j] - p[imin1] == 0 and jbest == 0 and ibest == 0:
            jbest = j
            ibest = imin1
        if p[j] < p[imin1] or imin1 == 0:
            imin1 = j
    else:
        if (p[j] - p[imin2]) % 3 == 0 and p[j] - p[imin2] > p[jbest] - p[ibest]:
            jbest = j
            ibest = imin2
        elif p[j] - p[imin2] == 0 and jbest == 0 and ibest == 0:
            jbest = j
            ibest = imin2
        if p[j] < p[imin2] or imin2 == 0:
            imin2 = j

# print(p[j], imin0, imin1, imin2, ibest, jbest, p[jbest] - p[ibest])
if jbest == 0:
    print(-1)
else:
    print(ibest + 1, jbest)

--------------------------------

import re

s = 'sdfa $500 400$ sdfdf $300$ dsg'

print(re.search('\d+(?=\$)', s)[0])
print(re.search('(?<=\$)\d+', s)[0])

--------------------------------
import re

s = 'https://www.youtube https://yandex.ru/search/?clid=9582&text=регулярное+выражение+адрес+сайта&l10n=ru&lr=2'

print(re.search('(http|https)(://)([a-zA-Z0-9.-_]+)\.(ru|com)', s)[0])

--------------------------------

import re

s = 'Привет! Как вы там? Увидимся'

print(re.search('^Привет', s)[0])
print(re.search('Увидимся$', s)[0])
print(re.search('^Привет|Увидимся$', s)[0])
print(re.search('[а-яА-Я]{8}', s)[0])

--------------------------------

dct = {1: 9, 2: 5, 3: 7, 4: 9}
print(min(dct, key=lambda x: (-dct[x], x)))
print(min(dct.keys(), key=lambda x: (-dct[x], x)))
print(sorted(dct, key=lambda x: (-dct[x], x)))
print(sorted(dct.keys(), key=lambda x: (-dct[x], x)))

--------------------------------

def division(a, b):
    return a / b

print(division(10, -2))

--------------------------------
import os

# os.mkdir('DELETE')
# os.chdir('./DELETE')
# os.chdir('..')
# os.chdir('./current')
# os.chdir('./DELETE')
# os.mkdir('DEL')
os.chdir('./DELETE')
print(os.getcwd())
os.remove('DEL')
print(os.getcwd())
print(*os.listdir(), sep='\n')

--------------------------------

import requests

url = 'https://httpbin.org/headers'
response = requests.get(url)

print(response.headers)

--------------------------------

from sys import getsizeof
lst = [1, 2, 3, 4]
print(getsizeof(lst))
lst = ['dsjfhglkdha', 'sadhfkjls', 'adhfkjsdhsdafgdsgs', 'sdgakjdfg']
print(getsizeof(lst))
lst = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
print(getsizeof(lst))
lst = [[1, 2, 3, 4], 'fdgfd', 5, {x: x**2 for x in range(1000)}]
print(getsizeof(lst))






"""
https://www.youtube.com/c/FeyginLive/videos
https://www.youtube.com/c/arestovych/videos
https://www.youtube.com/channel/UC111NXlcDs0VGfyre6EiPmA/videos Zhd
https://www.youtube.com/c/MackNack/videos
https://www.youtube.com/c/maxkatz1/videos
https://www.youtube.com/channel/UCzaqqlriSjVyc795m86GVyg/videos Laty
https://www.youtube.com/c/NavalnyLiveChannel/videos
https://www.youtube.com/user/BananDW  ktznew
https://www.youtube.com/channel/UCWAIvx2yYLK_xTYD4F2mUNw/videos ZhGv
https://www.youtube.com/c/SergeyAleksashenkoSr/videos
https://www.youtube.com/channel/UCL1rJ0ROIw9V1qFeIN0ZTZQ/videos Shul
https://www.youtube.com/c/popularpolitics/videos
https://www.youtube.com/c/tvrain/videos
https://www.youtube.com/channel/UCBzDAjLfvBUBVMMP6-K-y0w/videos
"""

"""
https://web.telegram.org/z/#-1000150092 сит
https://web.telegram.org/z/#-1223675293 твиттер
https://t.me/zvizdecmanhustu уаналитик
https://web.telegram.org/z/#-1074354585 военный осведомитель
Рыбарь
Два майора
"""

"""
карты
https://deepstatemap.live
https://liveuamap.com
https://www.google.com/maps/d/viewer?mid=1lscRK6ehG0l2V-XvJ16nsyblMsQ&hl=en_US&ll=49.622124783582485%2C32.41804124113801&z=7
https://twitter.com/War_Mapper
"""

"""
https://www.youtube.com/c/IvanYakovina/videos
https://www.youtube.com/c/NevzorovTV/videos
https://www.youtube.com/c/ivarlamov/videos
https://www.youtube.com/c/Редакция/videos
"""

'''
