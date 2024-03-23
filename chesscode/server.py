from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        #ip adress of my mac, socket
        serversocket.bind(('192.168.1.230', 5555))

        serversocket.listen(2)
        while True:
            print('Hola')
            (clientsocket, adress) = serversocket.accept()
            #running if someone has accepted
            rd = clientsocket.recv(2048).decode('utf-8')
            print(rd)
            #make sure we can send things
            #make sure we can recieve things
            data = 'hello world'
            clientsocket.sendall(str(data).encode('utf-8'))
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

    




