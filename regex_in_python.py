import re

match = re.match(input(), input())
if match:
    print(match.group(0))


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



"""