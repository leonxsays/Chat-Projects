import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'localhost'

def pscan(port):
    #can connect
    try:
        s.connect((server,port))
        return True
    #cant connect
    except:
        return False

#test range 1-25
#very slow, threading it is faster
for x in range(1,26):
    if pscan(x):
        print('Port',x,'is open!!!')
    else:
        print('Port',x,'is closed')

