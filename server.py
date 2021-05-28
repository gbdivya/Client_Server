import socket

ServerSocket = socket.socket()

print("Socket Created")
host= '192.168.246.45'
port= 3000

ServerSocket.bind((host,port))
ServerSocket.listen(5)

print('Waitiing for a Connection..')

while True:
    ClientSocket, addr = ServerSocket.accept()
    name = ClientSocket.recv(1024).decode()
    print( name, ": Connected" )
    ClientSocket.close()
