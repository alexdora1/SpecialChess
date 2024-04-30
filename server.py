from socket import *
from threading import *
import random

Header = 64
serversocket = socket(AF_INET, SOCK_STREAM)
#server is bount to Dean's mac
#ADDR = ('172.27.8.183', 5555)
ADDR = ('172.27.8.183', 14000)
serversocket.bind(ADDR)
computers = []
global Thread_List
Thread_List = []
First_Moves = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']

Names = ['Mark', 'Alex', 'Matt', 'Collin', 'Christoph', 'Anna', 'Rob', 'Annie', 'Phredrick', 'olamma', 'lambda', 'jeremy', '@$%!', 'Jerome', 'Jemmy', 'Bilbo', 'Hobbit']
ultraPieces = []
def extra(msg):
    number = len(msg)
    filler = ''
    i = 0
    while i != number:
        filler += '_'



def client_interact(conn, addr):
    print('NEW CONNECTION', addr, 'connected')
    connected = True
    firstMove = True
    index = computers.index(conn)

    #sends teams to client side
    if computers.index(conn) % 2 == 0:
        team = 'team*r*'
        sending = Names[index] + ' (self / red) vs. ' + Names[index + 1] + ' (opponent / green)*'
        team += sending
        team = team.encode()
        conn.send(team)

        print('sent', team)
        #This selects the ultra pieces
        redUltra = str(random.randint(0, 11))
        greenUltra = str(random.randint(12, 35))
        ultraPieces.append(redUltra)
        ultraPieces.append(greenUltra)
        sending = '^redUltra^' + redUltra + '^greenUltra^' + greenUltra + '^'
        conn.send(sending.encode())
    else:
        team = 'team*g*'
        sending = Names[index] + ' (self / green) vs. ' + Names[index - 1] + ' (opponent / red)*'
        team += sending
        print('sent', team)
        team = team.encode()
        conn.send(team)
        #This sends the ultra Pieces to
        sending = '^redUltra^' + ultraPieces[index - 1] + '^greenUltra^' + ultraPieces[index]  + '^'        
        if First_Moves[index - 1] != '_':
            sending += (First_Moves[index - 1])
        print('Sent', sending)
        conn.send(sending.encode())
    #gets messages, sends messages to
    while connected:
        msg = conn.recv(50).decode()
        print(addr, " sent:", msg)

        if firstMove:
            First_Moves[index] = (msg)
            print('First Move: ', First_Moves[index])
            firstMove = False
        if len(computers) > 1 and computers.index(conn) % 2 == 0:
            computers[(computers.index(conn) + 1)].send(msg.encode())
        elif len(computers) > 1 and computers.index(conn) % 2 != 0:
            computers[index - 1].send(msg.encode())
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
                    First_Moves[index + 1] = '_'
                    First_Moves[index] = '_'
                    computers.pop(computers.index(conn) + 1)
            elif len(computers) > 1 and computers.index(conn) % 2 != 0:
                computers[(computers.index(conn) - 1)].send(sendoff)
                computers[(computers.index(conn) - 1)].close()
                First_Moves[index - 1] = '_'
                First_Moves[index] = '_'
                computers.pop(computers.index(conn) - 1)
            computers.pop(computers.index(conn))
            conn.close()



def start():
    serversocket.listen()
    try:
        conn, addr = serversocket.accept()
        computers.append(conn)
        thread = Thread(target = client_interact, args=(conn,addr))
        Thread_List.append(thread)
        thread.start()
    except KeyboardInterrupt:
        print('Code killed')
        


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








