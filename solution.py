from sys import getsizeof
from pympler import asizeof

name = {300, 301, 302}

print(getsizeof(name), asizeof.asizeof(name))
