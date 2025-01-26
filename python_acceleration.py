import sys

_ = int(input())
lst = list(map(int, sys.stdin.readlines()))
# прекращение ввода в пайчарме - Ctrl + D

print(sum(lst))

'''
-----------------

from sys import setrecursionlimit
import threading


def factorial(n, mod):
    if n == 0:
        return 1
    return (n * factorial(n - 1, mod)) % mod


def main():  # наша программа
    mod = 10**9 + 7
    n = int(input())
    res = factorial(n, mod)
    print(res)


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)  # лучше использовать именно эту константу
thread = threading.Thread(target=main)
thread.start()
'''
