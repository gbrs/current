dct = {1: 9, 2: 5, 3: 7, 4: 9}
print(min(dct, key=lambda x: (-dct[x], x)))
print(min(dct.keys(), key=lambda x: (-dct[x], x)))
print(sorted(dct, key=lambda x: (-dct[x], x)))
print(sorted(dct.keys(), key=lambda x: (-dct[x], x)))


'''
--------------------------------


--------------------------------


--------------------------------


--------------------------------


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

--------------------------------

list_2D = [[4, 5, 6, 7], [2, 3], [1], []]
answer = sum(map(len, list_2D))
answer = sum([len(i) for i in list_2D])
answer = sum(list_2D, key=len)
print(answer)

--------------------------------

st = set()
for x in range(15):
    st.add(x)
for x in range(20, 5, -1):
    st.add(x)
st.pop()
print(st)


--------------------------------

dct = {}
for x in range(20, 10, -1):
    dct[x] = x**2
for x in range(10):
    dct[x] = x ** 2
dct = sorted(dct.items(), key=lambda item: [item[0], item[1]])
print(dct)

--------------------------------

def foo(y):
    y.append(6)
    return y


x = [5]
print(foo(x))
print(x)

--------------------------------

print([*{1: 1, 2: 4, 3: 9}.items()])
print(dict([(1, 1), (2, 4), (3, 9)]))

--------------------------------

import random

print(*sorted([random.normalvariate(0, 1) for _ in range(100)]), sep='\n')

--------------------------------

from itertools import product
[print(*i, sep='', end=' ') for i in list(product('ABC', 'XYZ'))]

--------------------------------

from functools import reduce
s = 'aFmbkSfHdGlFHfhcAFGDYHBB'
print(reduce(lambda count, item: count + ('a' <= item <= 'z'), s, 0))

-------------------

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
https://web.telegram.org/z/#-1634647964 уаналитик
https://web.telegram.org/z/#-1074354585 военный осведомитель
"""

"""
https://www.youtube.com/c/IvanYakovina/videos
https://www.youtube.com/c/NevzorovTV/videos
https://www.youtube.com/c/ivarlamov/videos
https://www.youtube.com/c/Редакция/videos
"""

'''
