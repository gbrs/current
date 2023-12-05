'''
(?<=href=['\"]).+?(?=['\"])
(?<=<a).+?(?=</a>)
'''

import re

s = '''
        <html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" 
        content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Пролистай вниз</title><link rel="stylesheet" href="./css/normalize.css">
        <link rel="stylesheet" href="./css/style.css"><link rel="icon" href="./img/icon.jpg">
        </head><body><header><h1 class="privet">Привет!<br>Пролистай страничку вниз.
        </h1><img src="./img/photo.jpg" alt="" class="logo_icon">
        </header><main><p class="paragraph">Чтобы продолжить - отправь боту любое фото.
        </p></main><footer><a class="link" href="./img/photo.jpg" download="">Фото</a>
        <p class="link">id стикера - CAACAgIAAxkBAAIDxWITCaZnaUelQ0SNlHMTrjd2klAmAAIBAQACVp29CiK-
        nw64wuY0IwQ</p><a class="link" href="./img/tochno.txt" download="">Документ</a></footer></body></html>
'''

lst1 = re.findall(r"(?<=<a).+?(?=</a>)", s)

# [print(date) for date in lst1]

lst2 = [re.search(r"(?<=href=['\"]).+?(?=['\"])", x) for x in lst1]

[print(date.group(0)) for date in lst2]



"""
Код из курса "Регулярные выражения в Python"
https://stepik.org/course/107335/syllabus
----------------
3.2.1
import re
reg = r'\b[А-Яа-я]+\b'
s = 'Второй тест'
match = re.match(reg, s)
print(match.group(0))
print(match.start())
print(match.end())
print(match.pos)
print(match.endpos)
print(match.re)
print(match.string)


3.2.2
import re
match = re.match(input(), input())
if match:
    print(match.group(0))


3.3.1
import re

search = re.search(r'#[a-z]+', input())
if search:
    print(search.group(0))


3.3.2
import re
for i in range(1, 5):
    search = re.search(r'[Кк]од', input().strip())
    if search:
        print(i, search.span()[0])
        break
else:
    print('код не найден')


3.3.3
import re

for i in range(5):
    search = re.search(r'(?<=Activation key: )([A-Z0-9]{5}-){4}[A-Z0-9]{5}', input().strip())
    if search:
        print(search.group(0))
        break


3.3.4
import re
search = re.search(r't=[\w.\+]+', input().strip())
print(search.group(0))


3.4.1
import re
search = re.match(r'[A-Za-z]+', input().strip())
if search:
    print(f'Первое слово в предложении: {search.group(0)}')


3.4.2
import re
search = re.match(r'([a-z]+ ){11}[a-z]+', input().strip())
if search:
    print('Возможно, это seed-фраза')


3.4.3
import re

search = re.match(r'.+(?=@)', input().strip())
print(search.group(0))


3.5.1
import re

search = re.fullmatch(r'\d{13,}', input().strip())
print(True if search else False)


3.5.2
import re

search = re.fullmatch(r'[a-zA-Z0-9@#$%^&*()_\-+!?]{8,}', input().strip())
print(True if search else False)


3.5.3
import re

search = re.fullmatch(r'\+?(?:[0-9][ ()-]{0,2}){11}', input().strip())
print(True if search else False)


3.5.4
(?:\d*x?\^?\d?[+-]*\b)+  НЕ РАБОТАЕТ

3.6.1
import re

s = 'يحتاج الجسم القوي إلى عقل قوي'

answer = re.finditer(r"\w+", s)

for word in answer:
    print(word.group(0))

3.6.2
import re

s = '''Мы вынуждены отталкиваться от того, что разбавленное изрядной долей эмпатии, 
        рациональное мышление способствует подготовке и реализации модели развития. 
        В целом, конечно, консультация с широким активом предоставляет широкие 
        возможности для форм воздействия.'''

answer = re.finditer(r"\b[A-Za-zА-Яа-яЁё]{5}\b", s)

for word in answer:
    print(word.group(0))

print(*answer, sep='\n')  # другой вариант

3.6.3
import re

s = '''</div></div><div class="main-indicator_rate"><div class="col-md-2 col-xs-9 _dollar">USD</div><div class="col-md-2 col-xs-9 _right mono-num">74,9990 ₽</div><div class="col-md-2 col-xs-9 _right mono-num">73,5050 ₽</div><div class="main-indicator_tooltip" id="V_R01235"><div class="main-indicator_tooltip-head"><button class="main-indicator_tooltip-head-btn _left "></button><div class="main-indicator_tooltip-head-text">19.04.2022 - 23.04.2022</div><button class="main-indicator_tooltip-head-btn _right _disabled "></button></div><table class="main-indicator_tooltip-table"><tr><td class="_day">вт</td><td class="_date">19.04</td><td>79,4529&nbsp;₽</td><td class="_green">-0,5908&nbsp;₽</td></tr><tr><td class="_day">ср</td><td class="_date">20.04</td><td>79,0287&nbsp;₽</td><td class="_green">-0,4242&nbsp;₽</td></tr><tr><td class="_day">чт</td><td class="_date">21.04</td><td>77,0809&nbsp;₽</td><td class="_green">-1,9478&nbsp;₽</td></tr><tr><td class="_day">пт</td><td class="_date">22.04</td><td>74,9990&nbsp;₽</td><td class="_green">-2,0819&nbsp;₽</td></tr><tr><td class="_day">сб</td><td class="_date">23.04</td><td>73,5050&nbsp;₽</td><td class="_green">-1,4940&nbsp;₽</td></tr></table><div class="main-indicator_tooltip-footer">Официальный курс Банка России</div></div></div><div class="main-indicator_rate"><div class="col-md-2 col-xs-9 _euro">EUR</div><div class="col-md-2 col-xs-9 _right mono-num">81,2239 ₽</div><div class="col-md-2 col-xs-9 _right mono-num">80,0249 ₽</div>'''

answer = re.finditer(r"\d+,\d+ ₽", s)

for word in answer:
    print(word.group(0))

# лепота:
# for i in re.finditer(r'\d{2,},\d{4} ₽', input()):
#     print(i[0])


3.7.1
[print(password)  for password in re.findall(r"https://imgur\.com/[A-Za-z0-9]{7}", input())]


3.7.2
import re
s = input()
[print(address) for address in re.findall(r"\s[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+\b", s)]


3.7.3
import re
s = input()
[print(date)
        for date
        in re.findall(
                r"\d{2}/\d{2}/\d{4}|\d{4}/\d{2}/\d{2}|\d{2}\.\d{2}\.\d{4}|\d{4}\.\d{2}\.\d{2}",
                s
        )
 ]


3.7.4
import re

s = input()

[print(date) for date in re.findall(r"\b(?:[01][0-9]:[0-5][0-9])|(?:[2][0-3]:[0-5][0-9])\b", s)]


3.7.5
import re

s = input()

lst1 = re.findall(r"(?<=<a).+?(?=</a>)", s)
lst2 = [re.search(r"(?<=href=['\"]).+?(?=['\"])", x) for x in lst1]
[print(date.group(0)) for date in lst2]




"""
