import socket

class Network:
    def __init__(self):
        socket.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.205'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
    def connect(self):
        try: 
            self.cliant.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

n = Network()

