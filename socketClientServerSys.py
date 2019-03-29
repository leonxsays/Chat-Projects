import socket
import sys
from _thread import *

host = ''
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((host,port))

except socket.error as e:
    print(str(e))

#listening for 5 connections queue
s.listen(5)
print('Waiting for connection...')
def threaded_client(conn):
    #Python 3 encode before you send, decode after you rec
    conn.send(str.encode('Welcome, type your info\n'))

    #keep connection
    while True:
        data = conn.recv(1024)
        reply = 'Server output: ' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:
    conn,addr = s.accept()
    print('connected to: ' + addr[0] + ':' + str(addr[1]))

    start_new_thread(threaded_client,(conn,))
