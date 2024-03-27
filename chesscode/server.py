from socket import *
from threading import *

Header = 64
serversocket = socket(AF_INET, SOCK_STREAM)
ADDR = ('192.168.1.205', 5555)
serversocket.bind(ADDR)
computers = []


def client_interact(conn, addr):
    print('NEW CONNECTION', addr, 'connected')
    connected = True
    #sends teams to client side
    if computers.index(conn) % 2 == 0:
        team = 'r'
        conn.send(team.encode())
    else:
        team = 'g'
        conn.send(team.encode())
    #gets messages, sends messages to
    while connected:
        msg = conn.recv(21).decode()
        print(addr, " sent:", msg)
        if len(computers) > 1 and computers.index(conn) % 2 == 0:
            computers[(computers.index(conn) + 1)].send(msg.encode())
        elif len(computers) > 1 and computers.index(conn) % 2 != 0:
            computers[(computers.index(conn) - 1)].send(msg.encode())
        else:
            conn.send(msg.encode())
        print('sent', msg)
        #closes connections of players who were playing together if their opponent quit
        if msg == 'BYEBYEBYEBYEBYEBYEBYE':
            connected =False
            sendoff = 'your opponent quit'
            sendoff = sendoff.encode()
            if len(computers) > 1 and computers.index(conn) % 2 == 0:
                    computers[(computers.index(conn) + 1)].send(sendoff)
                    computers[(computers.index(conn) + 1)].close()
                    computers.pop(computers.index(conn) + 1)
            elif len(computers) > 1 and computers.index(conn) % 2 != 0:
                computers[(computers.index(conn) - 1)].send(sendoff)
                computers[(computers.index(conn) - 1)].close()
                computers.pop(computers.index(conn) - 1)
            computers.pop(computers.index(conn))
            conn.close()



def start():
    serversocket.listen()
    while True:
        conn, addr = serversocket.accept()
        computers.append(conn)
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








