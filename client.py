import socket

ClientSocket = socket.socket()
host= '192.168.246.45'
port= 3000
ClientSocket.connect((host,port))

name = input('Write Something: ')
ClientSocket.send(bytes(name, 'utf-8'))

print(ClientSocket.recv(1024).decode())
