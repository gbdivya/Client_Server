import socket

ServerSocket = socket.socket()

print("Socket Created")
HOST= socket.gethostname()   
PORT= 5000
ServerSocket.bind((HOST,PORT))
ServerSocket.listen(5)

print('Waitiing for a Connection..')
print("\n")

while True:
    ClientSocket, addr = ServerSocket.accept()
    name = ClientSocket.recv(1024).decode()
    print('Connected by : ', name, addr )
    message = ClientSocket.recv(1024).decode()
    print('Message is : ', message)
    #filename=input(str("Enter the file name: "))
    filename=ClientSocket.recv(1024).decode()
    file=open(filename,'rb')
    file_data=file.read(1024)
    ClientSocket.send(file_data)
    print("Done sending")
    print("\n")
    
    ClientSocket.close()
