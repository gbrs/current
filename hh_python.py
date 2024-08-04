def score(cf: float, *scores: list):
    for i in scores:
        print(cf * i)


cf = 0.2
scores = [4, 5, 4]
score(cf, scores)

"""



--------------------



--------------------



--------------------



--------------------



--------------------



--------------------



--------------------



--------------------



--------------------



--------------------



--------------------



--------------------

14
from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def move(self):
        self


class Queen(Piece):
    def move(self):
        print('fdgsg')


a = Piece()
b = Queen()
a.move()
b.move()

Can't instantiate abstract class Piece with abstract method move

--------------------

7
def score(cf: float, *scores: list):
    for i in scores:
        print(cf * i)


cf = 0.2
scores = [4, 5, 4]
score(cf, scores)

can't multiply sequence by non-int of type 'float'

--------------------

3
d = {1: 1, 2: 4, 4: 16}

d.pop(4)
d.setdefault(0, 0)
d.sorted()

print(d)

'dict' object has no attribute 'sorted'

--------------------

x = 5
print('x =', x + 3)
print(x)

5

--------------------

a = 5
b = 10

print(a = b)

'a' is an invalid keyword argument for print()
но в ответах на хх была только ошибка тайпэррор

"""



