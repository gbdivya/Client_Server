import socket

ClientSocket = socket.socket()
HOST= socket.gethostname() 
PORT= 5000
ClientSocket.connect((HOST,PORT))
print("Connected Successfully")

name = input('Write your name: ')
ClientSocket.send(bytes(name, 'utf-8'))


message = input('Write your message: ')
ClientSocket.send(bytes(message, 'utf-8'))

filename=input(str("Enter the file name: "))
ClientSocket.send(bytes(filename, 'utf-8'))

file=open(filename,'wb')
file_data=ClientSocket.recv(1024)
file.write(file_data)
file.close()
print("File received")
print('connection closed')

print(ClientSocket.recv(1024).decode())
