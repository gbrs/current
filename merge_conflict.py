from sys import getsizeof

lst = [1, 2, 3, 4]
print(getsizeof(lst))
lst = ['dsjfhglkdha', 'sadhfkjls', 'adhfkjsdhsdafgdsgs', 'sdgakjdfg']
print(getsizeof(lst))

lst = [[1, 2, 3, 4], 'fdgfd', 5, {x: x ** 2 for x in range(1000)}]
print(getsizeof(lst))

lst = [{x: x ** 2 for x in range(1000)},
       {x: x ** 2 for x in range(1000)},
       {x: x ** 2 for x in range(1000)},
       {x: x ** 2 for x in range(1000)}]
print(getsizeof(lst))

print('фильм тугади')
