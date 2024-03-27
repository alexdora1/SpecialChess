from socket import *
from threading import *

Header = 64
serversocket = socket(AF_INET, SOCK_STREAM)
ADDR = ('192.168.1.230', 5555)
serversocket.bind(ADDR)
computers = []


def client_interact(conn, addr):
    print('NEW CONNECTION', addr, 'connected')
    connected = True
    while connected:
        msg = conn.recv(21).decode()
        print(addr, " sent:", msg)
        conn.send(msg.encode())
        print('sent', msg)
        if msg == 'BYEBYEBYEBYEBYEBYEBYE':
            connected =False
    conn.close()



def start():
    serversocket.listen()
    while True:
        conn, addr = serversocket.accept()
        thread = Thread(target = client_interact, args=(conn,addr))
        thread.start()

    
print('Server is starting')
start()

'''
def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        #ip adress of my mac, socket


        serversocket.bind(('192.168.1.230', 5555))

        serversocket.listen(2)
        while True:

            (clientsocket, adress) = serversocket.accept()
            #running if someone has accepted
            rd = clientsocket.recv(2048).decode()
            print(rd)
            #make sure we can send things
            #make sure we can recieve things
            data = 'hello world'
            clientsocket.sendall(str(data).encode())
            clientsocket.shutdown(SHUT_WR)
            #splitting
    except KeyboardInterrupt:
        print('\nShutting down...\n')
    except Exception as exc:
        print('Error: \n')
        print(exc)
    serversocket.close()

print('Starting...')
createServer()

''' 




