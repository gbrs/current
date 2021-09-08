'''
Простейший сервер. Создается, слушает, в ответ на запрос бросает ответ
'''

'''
https://docs.python.org/3/library/socket.html
'''


import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# сервер привязываем к сокету
server.bind(('127.15.4.72', 1504))
# сервер слушает. Очередь из четверых клиентов максимум
server.listen(4)
print('Ждем-с...')

# в браузере вводим: http://127.15.4.72:1504/request

# "сокетный объект клиента" и его адрес
client_socket, address = server.accept()
# принимаем от клиента максимум 1024 байта информации
data = client_socket.recv(1024).decode('utf-8')
print(data)

HEDER = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
content = 'Есть контакт!'.encode('utf-8')
# без хедера некоторые браузеры (например,хром) ничего не покажут
client_socket.send(HEDER + content)
