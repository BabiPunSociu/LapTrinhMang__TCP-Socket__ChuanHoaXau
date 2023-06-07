# Client
import socket
host = 'localhost'
port = 9050
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect((host,port))
data = sk.recv(1024)    # Nhan 1
print(data.decode('utf-8'))
while True:
    data = input('Nhap message: ')
    sk.send(data.encode('utf-8'))   # Gui 2
    data = sk.recv(1024)    # Nhan 3
    print(data.decode('utf-8'))
    if data.decode('utf-8') == 'Bye.':
        sk.close()
        break