'''
Создайте класс Бакалея.
В переменных укажите количество в килограммах.
Также добавьте метод Готовить, в результате вызова которого для объекта класса Бакалея,
будет выводится сообщение о начале приготовления.

Создайте дочерний класс от класса Бакалея - Консервы.
Укажите в качестве переменных (помимо унаследованных):
название,
необходимость приготовления (можно есть сразу или нужно приготовить),
категорию - рыбные/мясные/другие.
Также добавьте метод Открыть (помимо существующего метода),
в результате работы которого будет выведено на экран сообщение об открытии банки консервов.

Создайте дочерний класс от класса Бакалея - Каши.
Укажите в качестве переменных (помимо унаследованных):
название,
необходимость варки (варить или другой способ приготовления),
необходимость промыть перед готовкой (надо или не надо),
можно ли есть с молоком (да или нет).
Также добавьте метод Эксперимент (помимо существующего метода),
в результате работы которого будет выведено на экран сообщение о необычном блюде из любой крупы.

Продумайте план тестирования и протестируйте созданные классы
(создайте объекты,
выведите на экран,
проверьте работоспособность методов).
'''


class Grocery:

    def __init__(self, mass):
        self.quantity = mass

    def cook(self):
        print(f'Начинаю приготовление: {self.name}')


class Preserves(Grocery):

    def __init__(self, mass, name, is_cooked, category):
        super().__init__(mass)
        self.name = name
        self.is_cooked = is_cooked
        self.category = category

    def open(self):
        print(f'Открываю банку консервов: {self.name}')


class Porridge(Grocery):

    def __init__(self, mass, name, is_cooked, is_washed, is_milked):
        super().__init__(mass)
        self.name = name
        self.is_cooked = is_cooked
        self.is_washed = is_washed
        self.is_milked = is_milked

    def experiment(self):
        print(f'А теперь шашлык из крупы: {self.name}')


print('Проверим класс круп')
rice = Porridge(10, 'рис', False, False, True)
rice.cook()
rice.experiment()
print(f'{rice.name}. {rice.quantity} кг.')
print(f'Нуждается в приготовлении? {not rice.is_cooked}.')
print(f'Нуждается в промывке? {not rice.is_washed}.')
print(f'Может готовиться с молоком? {rice.is_milked}.')
print()

print('Проверим класс консервов')
sprat_in_tomato_sauce = Preserves(0.280, "Килька в томатном соусе", True, 'рыбные')
sprat_in_tomato_sauce.cook()
sprat_in_tomato_sauce.open()
'mass, name, is_cooked, category'
print(f'{sprat_in_tomato_sauce.name}. {int(sprat_in_tomato_sauce.quantity * 1000)} гр.')
print(f'Нуждается в приготовлении? {not sprat_in_tomato_sauce.is_cooked}.')
print(f'Тип консервов: {sprat_in_tomato_sauce.category}')

'''
Продумайте план тестирования и протестируйте созданные классы
(создайте объекты,
выведите на экран,
проверьте работоспособность методов).
'''

'''
--------------------------------



--------------------------------

"""
Создайте класс Товар, который будет содержать переменные: название товара, артикул.

Создайте класс Категория товара, который будет содержать переменные: название категории, товары в категории.
Также необходимо реализовать метод, который позволит добавлять товары (объект класса Товар) в категорию (список).

Далее создайте класс Пользователь, который будет содержать переменные: имя пользователя, любимые категории.
Добавьте метод, который позволит "ставить лайк" категории товара (то есть объекту класса Категория товара).
Поставить лайк - это добавить категорию в список любимых категорий.

Далее реализуйте сценарий, в котором:

Добавляем 2 произвольных товара
Затем создаем 1 категория
Далее в категорию добавляем 2 товара
Добавляем 3 произвольных товара
Создаем еще 2 категории
В одну из новых категорий добавляем все 3 новых товара
Затем выводим на экран содержимое всех 3 категорий
Создаем пользователя
Добавляем в любимые категории пользователя 2 произвольные категории и выводим их на экран
"""

# создаем три класса
class Goods:
    def __init__(self, name, code):
        self.goods_name = name
        self.vendor_code = code


class GoodsCategory:
    def __init__(self, name):
        self.category_name = name
        self.category_goods = []

    def add_goods(self, goods):
        self.category_goods.append(goods)


class User:
    def __init__(self, name):
        self.user_name = name
        self.favorite_categories = []

    def like_category(self, category):
        self.favorite_categories.append(category)


# создаем 2 товара, класс для них и добавляем товары в класс
jeans = Goods('jeans', '4242')
shirt = Goods('shirt', '2022')

clothes = GoodsCategory('clothes')
clothes.add_goods(jeans)
clothes.add_goods(shirt)

# создаем 3 товара, класс для них и добавляем товары в класс
w_and_p = Goods('War and Peace', '1869')
p_and_p = Goods('Pride and Prejudice', '1813')
m_and_m = Goods('Master and Margarita', '1967')

books = GoodsCategory('books')
books.add_goods(w_and_p)
books.add_goods(p_and_p)
books.add_goods(m_and_m)

# создаем третий класс, но не добавляем в него ничего
cars = GoodsCategory('cars')

# напечатаем товары, принадлежащие каждой категории
for category in (clothes, books, cars):
    print(category.category_name, end=': ')
    for goods in category.category_goods:
        print(goods.goods_name, end=', ')
    print()
# print(clothes.category_goods, books.category_goods, cars.category_goods, sep='\n')
print()

# создадим пользователя и добавим его две любимые категории
uzver = User('Uzverev Uzver Uzverevich')
uzver.like_category(clothes)
uzver.like_category(cars)

# напечатаем любимые категории пользователя
print(uzver.user_name, end=': ')
for category in uzver.favorite_categories:
    print(category.category_name, end=', ')

--------------------------------

"""
Создайте класс Товар, который будет содержать переменные: название товара, артикул.

Создайте класс Категория товара, который будет содержать переменные: название категории, товары в категории.
Также необходимо реализовать метод, который позволит добавлять товары (объект класса Товар) в категорию (список).

Далее создайте класс Пользователь, который будет содержать переменные: имя пользователя, любимые категории.
Добавьте метод, который позволит "ставить лайк" категории товара (то есть объекту класса Категория товара).
Поставить лайк - это добавить категорию в список любимых категорий.

Далее реализуйте сценарий, в котором:

Добавляем 2 произвольных товара
Затем создаем 1 категория
Далее в категорию добавляем 2 товара
Добавляем 3 произвольных товара
Создаем еще 2 категории
В одну из новых категорий добавляем все 3 новых товара
Затем выводим на экран содержимое всех 3 категорий
Создаем пользователя
Добавляем в любимые категории пользователя 2 произвольные категории и выводим их на экран
"""


# создаем три класса
class Goods:
    def __init__(self, name, code):
        self.goods_name = name
        self.vendor_code = code


class GoodsCategory:
    def __init__(self, name):
        self.category_name = name
        self.category_goods = []

    def add_goods(self, goods):
        self.category_goods.append(goods.goods_name)


class User:
    def __init__(self, name):
        self.user_name = name
        self.favorite_categories = []

    def like_category(self, category):
        self.favorite_categories.append(category.category_name)


# создаем 2 товара, класс для них и добавляем товары в класс
jeans = Goods('jeans', '4242')
shirt = Goods('shirt', '2022')

clothes = GoodsCategory('clothes')
clothes.add_goods(jeans)
clothes.add_goods(shirt)

# создаем 3 товара, класс для них и добавляем товары в класс
w_and_p = Goods('War and Peace', '1869')
p_and_p = Goods('Pride and Prejudice', '1813')
m_and_m = Goods('Master and Margarita', '1967')

books = GoodsCategory('books')
books.add_goods(w_and_p)
books.add_goods(p_and_p)
books.add_goods(m_and_m)

# создаем третий класс, но не добавляем в него ничего
cars = GoodsCategory('cars')

# напечатаем товары, принадлежащие каждой категории
print(clothes.category_goods, books.category_goods, cars.category_goods, sep='\n')
print()

# создадим пользователя и добавим его две любимые категории
uzver = User('Uzverev Uzver Uzverevich')
uzver.like_category(clothes)
uzver.like_category(cars)

# напечатаем любимые категории пользователя
print(uzver.favorite_categories)

--------------------------------

N = int(input())
p = [0]
jmin = 0
jmax = 1
imin = 0

for i in range(1, N + 1):
    # print(i, imin, jmin, jmax)
    p.append(p[i - 1] + int(input()))
    # print(p[i] - p[imin])
    if p[i] - p[imin] > p[jmax] - p[jmin]:
        jmin = imin
        jmax = i
    if p[i] <= p[imin]:
        imin = i
print(imin, jmin, jmax)
print(jmin + 1, jmax)

--------------------------------

import re

s = 'Имя: Борис. День рождения: 15 апреля 1972г.'
regex = r'Имя: ([а-яА-Я]+). День рождения: (\d+) ([а-яА-Я]+) (\d+)г?.?'
match = re.search(regex, s)
if match is not None:
    print(f'Имя: {match.group(1)}')
    print(f'Месяц рождения: {match.group(3)}')
else:
    print('Формат строки не совпадает')

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
'''
