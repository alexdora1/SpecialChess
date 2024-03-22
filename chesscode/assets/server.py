import socket
from _thread import *
import sys

#ip adress
server = '192.168.1.205'
#unused port
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(1)
print("Waiting for connection, server started")

def threaded_client(conn):
    conn.send(str.encode('Connected'))
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print('disconnected')
                break
            else:
                print('Recieved:', reply)
                print('sending', reply)
            #sending conn as byte object
            conn.sendall(str.encode(reply))
        except:
            break
    print('lost connection')
    conn.close()

    
#accepts incoming connections
while True:
    conn, addr = s.accept()
    #addr: IP adress
    print('connected to:', addr)
#threaded_client is running in the backround, will not interfere with while loop
    start_new_thread(threaded_client, (conn,))
