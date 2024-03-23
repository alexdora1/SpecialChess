import socket
from _thread import *
import sys
from main import *


#ip adress
server = '192.168.1.205'
#unused port
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, server started")
PosP = [(-1, -1), (-1, -1)]
net = Network()
def threaded_client(conn, current_player):
    print('waiting')
    Main(net)
    while True:

        Main()
        try:

            data = read_pos(conn.recv(2048).decode())

            reply = data('utf-8')

            if not data:
                print('disconnected')
                break
            else:
                if current_player == 1:
                    PosP[0] = data
                elif current_player == 2:
                    PosP[1] = data
                


                print('Recieved:', reply)
                print('sending', reply)
            #sending conn as byte object
            conn.sendall(str.encode(reply))
        except:
            break
    print('lost connection')
    conn.close()

net = Network()
#accepts incoming connections
currentPlayer = 0
rüber = True
while True:
    Input = ''
    Input = input()
    if input == 'stop':
        rüber = False

    print('waiting')

    Main(net)
    conn, addr = s.accept()
    #addr: IP adress
    print('connected to:', addr)
#threaded_client is running in the backround, will not interfere with while loop
    start_new_thread(threaded_client, (conn,))
    currentPlayer += 1
    print(currentPlayer)
