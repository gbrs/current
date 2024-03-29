import re
s = r'https://regex101.com/'
print(re.escape(s))



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



3.8.1
import re
s = "The first one is heavy!This actually goes really well with Chris's workout he's doing."
print(re.split(r"[.!?]", s))


3.8.2
import re
s = "Привет, как твои дела? Привет, нормально, учу регулярные выражения."
print(re.split(r"[.!?, ]", s))


3.8.3
import re
s = '''Категория: Телефоны\nSupreme Burner\nMotorola Razr\nКатегория: Смарт часы и браслеты\nApple Watch 6\nGarmin Venu\nXiaomi Mi Smart Band 6\nКатегория: Игры\nSpore'''
print(re.split(r"Категория: [А-Яа-яЁё ]+\n?", s))



3.9.1
import re
s = input()
print(re.split(r"Категория: [А-Яа-яЁё ]+\\n", s))


3.9.2
import re
s = '''<html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Timer ⏲</title><link rel="icon" href="./img/goes.png"><link rel="stylesheet" href="./css/normalize.css"><link rel="stylesheet" href="./css/style.css"></head><body><div class="time_wrapper"><h1 class="bold minutes">1:00:00</h1><img class="time" src="./img/start_end.png"></div><div class="buttons"><button class="buttons_button regular start" onclick="start()">Start</button><button class="buttons_button regular notshow pause" onclick="pause()">Pause</button></div></body>'''
print(''.join(re.split(r"<.*?>", s)))


3.10.1
import re
s = 'Maybe it’s my fault. Maybe I led you to believe it was easy, when it wasn’t. Maybe I made you think my highlights started at the free throw line, and not in the gym. Maybe I made you think that every shot I took was a game winner. That my game was built on flash, and not fire. Maybe it’s my fault that you didn’t see that failure gave me strength, that my pain was my motivation. Maybe I led you to believe that basketball was a God given gift, and not something I worked for, every single day of my life.'
print(re.subn(r"[.?!,:]", '', s)[-1])


3.10.2
import re
s = '65,905 views  Nov 19, 2022'
print(re.subn(r"[0-9]", 'X', s))


3.11.1
import re
s = r'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./0123456789:;'
print(re.escape(s))


3.11.2
import re
s = r'https://regex101.com/'
print(re.escape(s))

"""
