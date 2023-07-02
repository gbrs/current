import re

# сделать список строк?
text = ''
for _ in range(4):
    text = text + input() + '\n'

print(text)

search = re.search(r'[Кк]од', text)
print(search)
if search:
    print(search.span()[0])
else:
    print('код не найден')



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




"""