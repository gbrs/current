import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# сервер привязываем к сокету
server.bind(('127.15.4.72', 1504))
# сервер слушает. Очередь из четверых клиентов максимум
server.listen(4)

# прием соединений:
client_socket, address = server.accept()
data = client_socket.recv(1024).decode('utf-8')
print(data)

HEDER = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
content = 'Все прошло пучком!'.encode('utf-8')
client_socket.send(HEDER + content)
