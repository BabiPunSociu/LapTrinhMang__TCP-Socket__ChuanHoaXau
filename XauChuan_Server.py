# Xau Chuan
# Server
import socket

# Viet hoa chu cai dau tien, viet thuong cac chu cai con lai
def xuly1(str_):
    result =''
    for i in range(len(str_)):
            if str_[i] not in [' ',',','.']:
                if i==0:
                    result += str(str_[i]).upper()
                else:
                    result += str(str_[i]).lower()
            else:
                result += str_[i]
    return result

def cat_cham():
    global data
    list_ = []
    list_ = data.split('.')
    data =''
    for str_ in list_:
        str_ = str_.strip()
        if str_ != '':
            str_ = xuly1(str_)
            data += '. ' + str_
    data = data[2:] # Cat bo '. ' dau tien
    data.strip()
    return data

def cat_phay():
    global data
    list_ = []
    list_ = data.split(',')
    data = ''
    for str_ in list_:
        str_ = str_.strip()
        if str_ != '':
            data += ', ' + str_
    data = data[2:]
    data.strip()
    return data

def cat_daucach():
    global data
    list_ = []
    list_ = data.split(' ')
    data = ''
    for str_ in list_:
        if str_ != '':
            data += ' ' + str_ 
    data = data[1:]
    data.strip()
    return data

def chuanHoa():
    global data
    data = xuly1(data);
    data = cat_cham()
    data = cat_phay()
    data = cat_daucach()
    # Them '.' cuoi cau
    data += '.'
    return data
if __name__=='__main__':
    global data
    host = 'localhost'
    port = 9050
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((host,port))
    sk.listen(5)
    client_sk, client_addr = sk.accept()
    print('client address:',client_addr)
    data = 'hello client'
    client_sk.send(data.encode('utf-8'))    # Gui 1
    while True:
        data = client_sk.recv(1024)     # Nhan 2
        data = data.decode('utf-8')
        print('Ban dau:',data)
        data = chuanHoa()
        print('Da chuan hoa:', data)
        client_sk.send(data.encode('utf-8')) # Gui lai ket qua - Gui 3
        if data == 'Bye.':
            client_sk.close()
            break
        
