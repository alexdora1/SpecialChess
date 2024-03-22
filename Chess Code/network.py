import socket
import pygame
from main import drawpieces

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.205'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        
    def connect(self):
        try: 
            self.client.connect(self.addr)
            print(self.client.recv(2048).decode())
            return self.client.recv(2048).decode()
        except:
            return('(-1, -1)')
            pass
    def send(self, data):
        try:
          self.client.send(str.encode(data))
          return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

class Pieces:
    def __init__(self, image, loc):
        self.image = image
        self.loc = loc

#splits up the message
def findImages(message):
    pList = []
    tempList = message.split('$')
    for i in tempList:
        pieceDecon= i.split('|')
        pieceDecon[1].replace('(', '')
        pieceDecon[1].replace(')', '')
        loc = pieceDecon[1].split(',')
        pList.append(Pieces(pieceDecon, (int(loc[0]), int(loc[1]))))

def drawboard(screen):
  colors=[pygame.Color('green'),pygame.Color('red')]
  for r in range(9):
      for c in range(9):
        color=colors[(r+c)%2]
        pygame.draw.rect(screen, color, pygame.Rect(c*64,r*64,64,64))
  

net = Network()
(width, height) = (575, 575)
screen = pygame.display.set_mode((width, height))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            net.send(str(pos))
        elif event.type == pygame.QUIT:
            run = False
    drawboard(screen)
    if isinstance(net.connect(), str):
        images = findImages(net.connect())
        drawpieces(images)


