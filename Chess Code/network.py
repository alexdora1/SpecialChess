import socket
import pygame

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.205'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        
    def getPos(self):
        return self.pos
    def connect(self):
        try: 
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
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

def drawboard(screen):
  colors=[pygame.Color('green'),pygame.Color('red')]
  for r in range(9):
      for c in range(9):
        color=colors[(r+c)%2]
        pygame.draw.rect(screen, color, pygame.Rect(c*64,r*64,64,64))
  
def drawpieces(ex_board):
  for i in ex_board:
    screen.blit(pygame.image.load(i.image), (i.loc))

def findImages(message):
    pList = []
    tempList = message.split('$')
    for i in tempList:
        pieceDecon= i.split('|')
        pieceDecon[1].replace('(', '')
        pieceDecon[1].replace(')', '')
        loc = pieceDecon[1].split(',')
        pList.append(Pieces(pieceDecon, (int(loc[0]), int(loc[1]))))
        

net = Network()
runner = True
(width, height) = (575, 575)
screen = pygame.display.set_mode((width, height))
drawboard(screen)
while runner:
    pygame.display.flip()
    if net.connect() != None and net.connect() != '(-1, -1)':
        drawpieces(findImages(net.connect()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False


    pygame.display.update()