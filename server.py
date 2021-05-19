import socket

s = socket.socket()

print("Socket Created")

s.bind(('localhost', 3000))
s.listen(5)

print('waiting for connections')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with", addr, name)
    c.send(bytes("Welcome to MSIS", 'utf-8'))
    c.close()