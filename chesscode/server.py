from socket import *
from threading import *

Header = 64
serversocket = socket(AF_INET, SOCK_STREAM)
#server is bount to Dean's mac
ADDR = ('192.168.1.205', 5555)
serversocket.bind(ADDR)
computers = []
Player_Names = []

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
        conn.send(Player_Names[computers.index(conn) - 1].encode())
    #gets messages, sends messages to
    while connected:
        msg = conn.recv(50).decode()
        print(addr, " sent:", msg)
        if 'name' in msg:
            Player_Names.append(msg)
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
                    Player_Names.pop(computers.index(conn) + 1)
            elif len(computers) > 1 and computers.index(conn) % 2 != 0:

                computers[(computers.index(conn) - 1)].send(sendoff)
                computers[(computers.index(conn) - 1)].close()
                computers.pop(computers.index(conn) - 1)
                Player_Names.pop(computers.index(conn) + 1)
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