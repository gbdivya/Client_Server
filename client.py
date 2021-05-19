import socket

c = socket.socket()

c.connect(('localhost', 3000))

name = input("Enter client name \n")
c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())