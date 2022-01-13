from sys import getsizeof
lst = [1, 2, 3, 4]
print(getsizeof(lst))
lst = ['dsjfhglkdha', 'sadhfkjls', 'adhfkjsdhsdafgdsgs', 'sdgakjdfg']
print(getsizeof(lst))
lst = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
print(getsizeof(lst))
lst = [[1, 2, 3, 4], 'fdgfd', 5, {x: x**2 for x in range(1000)}]
print(getsizeof(lst))

'''


--------------------------------



--------------------------------

dct = {'a': 1, 'b': 2, 'c': 3}
d = dct.items()
print(type(d))

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

--------------------------------

# from functools import reduce
from memory_profiler import profile

@profile
def main():
    lst = [3 for _ in range(10**6)]
    result_count = len([1 for i in lst if i % 2 == 0])
    # result_count = reduce(lambda count, item: count + (item % 2 == 0), lst, 0)
    print(result_count)


main()

-------------------

arr = [12, 36, 23]
s = ':'.join(map(str, arr))  # выдаст 12:36:23
print(s)

-------------------

s = list('aaaaaaaaaaaaaa')
s[2:5:2] = list('AF')
print(s)
s[6:10] = ['A']
print(s)

-------------------

s = "b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'"
s = s.decode('utf-8')
print(s)

-------------------

from collections import namedtuple
Car = namedtuple('Car', ['color', 'mileage'])
my_car = Car('red', 3812.4)
print(my_car.color)

--------------------

import collections
s = "Установите"
c = collections.Counter(s)
print(c.most_common(10))

--------------------

lst1 = [[1, 2], [3, 4]]
lst2 = lst1
lst3 = [5, 6]
lst1[0] = lst3
lst3 = [7, 8]
print(lst1)
print(lst2)

--------------------

lst = [1, 3, 10]
[print(f'{item:->4}', end='') for item in lst]

--------------------

mile_distances = [1, 3, 10]
kilometer_distances = [x * 1.6 for x in mile_distances]
# kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))
print(kilometer_distances)
'''
