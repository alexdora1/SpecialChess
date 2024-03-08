import pygame
import time

#Adding a function to show the clicking

(width, height) = (575, 575)
screen = pygame.display.set_mode((width, height))

class Piece:
    def __init__(self, team, type, image, loc):
        self.team = team
        self.type = type
        self.image = image
        self.loc = loc

class Rook(Piece):
  def islegal(self, ex_board, pos1, pos2):
    return True

class Pawn(Piece):
  def islegal(self, ex_board, pos1, pos2):
    print(pos1)
    print(pos2)
    print(pos2[1] - pos1[1])                  
    if self.team == 'g':
      if pos1[1] == 64:
        #this is the only part that works
        if ((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (128)) and (pos2[1] - pos1[1] > 0)):
          return True
        elif ((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (64)) and (pos2[1] - pos1[1] > 0)):
          return True
      else:
        if((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (64)) and (pos2[1] - pos1[1] > 0)):
          return True
        elif (((pos1[0] - pos2[0] == 64) or (pos1[0] - pos2[0] == (-64))) and (pos2[1] - pos1[1]) == (64) and pos2[1] - pos1[1] > 0):
            for c in ex_board:
              if c.loc == (pos2[0], pos2[1]):
                ex_board.pop((ex_board.index(c)))
                return True
    else:
      if pos1[1] == 448:
        #this is the only part that works
        if ((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (-128)) and (pos2[1] - pos1[1] < 0)):
          return True
        elif ((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (-64)) and (pos2[1] - pos1[1] < 0)):
          return True
      else:
        if((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (-64)) and (pos2[1] - pos1[1] < 0)):
          return True
        elif (((pos1[0] - pos2[0] == 64) or (pos1[0] - pos2[0] == (-64))) and (pos2[1] - pos1[1]) == (-64) and pos2[1] - pos1[1] < 0):
            for c in ex_board:
              if c.loc == (pos2[0], pos2[1]):
                ex_board.pop((ex_board.index(c)))
                return True
    return False

        

#Assiging places 
        
gR1 = Piece('', '', '', (0,0))
gN1 = Piece('', '', '', (0,0))
gB1 = Piece('', '', '', (0,0))
gE = Piece('', '', '', (0,0)) 
gK = Piece('', '', '', (0,0))
gQ = Piece('', '', '', (0,0))
gB2= Piece('', '', '', (0,0))
gN2 = Piece('', '', '', (0,0))
gR2 = Piece('', '', '', (0,0))
gP1 = Pawn('', '', '', (0,0))
gP2 = Pawn('', '', '', (0,0))
gP3 = Pawn('', '', '', (0,0))
gP4 = Pawn('', '', '', (0,0))
gP5 = Pawn('', '', '', (0,0))
gP6 = Pawn('', '', '', (0,0))
gP7 = Pawn('', '', '', (0,0))
gP8 = Pawn('', '', '', (0,0))
gP9 = Pawn('', '', '', (0,0))
rP1 = Pawn('', '', '', (0,0))
rP2 = Pawn('', '', '', (0,0))
rP3 = Pawn('', '', '', (0,0))
rP4 = Pawn('', '', '', (0,0))
rP5 = Pawn('', '', '', (0,0))
rP6 = Pawn('', '', '', (0,0))
rP7 = Pawn('', '', '', (0,0))
rP8 = Pawn('', '', '', (0,0))
rP9 = Pawn('', '', '', (0,0))
rR1 = Piece('', '', '', (0,0))
rB1 = Piece('', '', '', (0,0))
rN1 = Piece('', '', '', (0,0))
rE = Piece('', '', '', (0,0))
rK = Piece('', '', '', (0,0))
rQ = Piece('', '', '', (0,0))
rB2 = Piece('', '', '', (0,0))
rN2 = Piece('', '', '', (0,0))
rR2 = Piece('', '', '', (0,0))

Pieces = [gR1, gN1, gB1, gE, gK, gQ, gB2, gN2, gR2, gP1, gP2, gP3, gP4, gP5, gP6, gP7, gP8, gP9, rP1,rP2,rP3,rP4,rP5,rP6,rP7,rP8,rP9,rR1,rN1,rB1,rE,rK,rQ,rB2,rN2,rR2]
def drawboard(screen):
  Piecewidth = 64 
  Pieceheight = 64

  colors=[pygame.Color('green'),pygame.Color('red')]
  for r in range(9):
      for c in range(9):
        color=colors[(r+c)%2]
        pygame.draw.rect(screen, color, pygame.Rect(c*64,r*64,64,64))
  


pieces_names = ["Rook", "Knight", "Boat", "Elephant", "King", "Queen", "Boat", "Knight", "Rook"]

#Creating Board
a =[]
b =[]
c =[]
d = [] 
e = []
f = []
g = []
h = []
i = []

#putting pieces in board with for loop. '_' is an unoccupied space
for i in range(0, 80):
  if i < 9:
    Pieces[i] = Piece("g", pieces_names[i],('assets/Green_' + pieces_names[i]+ '.png'), ((64*i), 0))
  elif 8 < i < 18:
   Pieces[i] = Pawn("g", 'Pawn',('assets/Green_Pawn.png'), ((64*(i-9), 64)))
  elif 17 < i  < 27:
    Pieces[i] = Pawn('r', 'Pawn', ('assets/Red_Pawn.png'), ((64*(i-18)), 64*7))
  elif 26 < i < 36:
    Pieces[i] = Piece('r', pieces_names[(i-27)], ('assets/Red_' + pieces_names[i-27]+'.png'), ((64*(i-27), 64*8)))



#putting board into the game
def drawpieces(ex_board):
  for i in ex_board:
    screen.blit(pygame.image.load(i.image), (i.loc))

move = 0
pygame.display.flip()

#Assigning positions for the mouse clicks using placeholder values (-1,-1) cannot be clicked
pos1 = [-1,-1]
pos2 = [-1, -1]

running = True
while running:
  drawboard(screen)
  drawpieces(Pieces)

  #We're going to need a shitload of logic here 
  #Find whose turn it is
  #Find which piece is being seleceted 
  #Find where the piece is being moved to  
  #Find if the move is legal 
  #Have it interact with other pieces
  #Checkmate 

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    #Recognizing first and second clicks 
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if pos1 == [-1,-1]:
        pos1 = pygame.mouse.get_pos()
        pos1 = [(pos1[0] - (int(pos1[0]) % 64)), pos1[1] - pos1[1] % 64]
        
        pos2 = [-1,-1]
      elif pos1 != [-1, -1]:
        pos2 = pygame.mouse.get_pos()
        pos2 = [(pos2[0] - pos2[0] % 64), (pos2[1] - pos2[1] % 64)] 
      

        for i in Pieces:
          if isinstance(i, Pawn) or isinstance(i, Rook):
            if (i.loc == (pos1[0], pos1[1])) and i.islegal(Pieces, pos1, pos2):
              
              pygame.draw.rect(screen, pygame.Color('blue'), pygame.Rect((pos1[0] - ((pos1[0]) % 64)), (pos1[1]-(pos1[1]%64)), 64, 64))
              i.loc = (pos2[0], pos2[1])
              pygame.draw.rect(screen, pygame.Color('purple'), pygame.Rect((pos2[0] - (pos2[0]) % 64), (pos2[1]-pos2[1]%64), 64, 64))
              drawpieces(Pieces)
          elif isinstance(i, Piece):
            if (i.loc == (pos1[0], pos1[1])):
              pygame.draw.rect(screen, pygame.Color('blue'), pygame.Rect((pos1[0] - ((pos1[0]) % 64)), (pos1[1]-(pos1[1]%64)), 64, 64))
              i.loc = (pos2[0], pos2[1])
              pygame.draw.rect(screen, pygame.Color('purple'), pygame.Rect((pos2[0] - (pos2[0]) % 64), (pos2[1]-pos2[1]%64), 64, 64))
              drawpieces(Pieces)
        
        pos1 = [-1,-1]
  
  #marking pieces 
  
  
  

  
  
  

  drawpieces(Pieces)


  pygame.display.update()