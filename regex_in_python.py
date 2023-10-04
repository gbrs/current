import re

s = 'يحتاج الجسم القوي إلى عقل قوي'

answer = re.finditer(r"\w+", s)

for word in answer:
    print(word.group(0))



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






"""
