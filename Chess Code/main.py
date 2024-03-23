import pygame
import time
from network import Network
#Adding a function to show the clicking

print('hello world')

(width, height) = (575, 575)
screen = pygame.display.set_mode((width, height))

clientNumber = 0

class Piece:
    def __init__(self, team, type, image, loc):
        self.team = team
        self.type = type
        self.image = image
        self.loc = loc
    def islegal(self, ex_board, pos1,pos2):
      print("We're in the piece")
      return True
    #this is so that one can easily send the pieces
    def toString(self):
      return(self.image + '|' + str(self.loc) + '$' )


class Rook(Piece):
    def islegal(self, ex_board, pos1, pos2):         
      if(pos1[0] < pos2[0]) and (pos2[1] == pos1[1]):
        # finds pieces                         
        for c in ex_board:
            if c.loc[1] == pos2[1] and pos1[0] < c.loc[0] < pos2[0]:
              return False
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True
      elif(pos2[0] < pos1[0]) and (pos2[1] == pos1[1]):
        # finds pieces                 
        for c in ex_board:
            if (c.loc[1] == pos2[1]) and (pos1[0] > c.loc[0] > pos2[0]):
              return False
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True
      elif(pos1[0] == pos2[0]) and (pos2[1] > pos1[1]):
        # finds pieces                     
        for c in ex_board:
            if c.loc[0] == pos2[0] and pos1[1] < c.loc[1] < pos2[1]:
              return False
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True
      elif(pos1[0] == pos2[0]) and (pos2[1] < pos1[1]):
        # finds pieces                     
        for c in ex_board:
            if c.loc[0] == pos2[0] and pos1[1] > c.loc[1] > pos2[1]:
              return False
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True 
      return False      

class Knight(Piece):
    def islegal(self, ex_board, pos1, pos2):   
      if((pos1[0] + 128 == pos2[0] or pos1[0] - 128 == pos2[0]) and (pos1[1] - 64 == pos2[1] or pos1[1] + 64 == pos2[1])) or ((pos1[1] + 128 == pos2[1] or pos1[1] - 128 == pos2[1]) and (pos1[0] - 64 == pos2[0] or pos1[0] + 64 == pos2[0])):
        for i in ex_board:
          if i.loc == (pos2[0], pos2[1]):
            if i.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(i))
              return True

        return True
      return False
    
class Boat(Piece):
    def islegal(self, ex_board, pos1, pos2):   
      if abs(pos2[0] - pos1[0]) == abs(pos2[1] - pos1[1]) and pos2[0] != pos1[0]:
        if pos1[0] > pos2[0] and pos1[1] > pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                return False
            x -= 64
            z -= 64
        elif pos1[0] < pos2[0] and pos1[1] > pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                return False
            x += 64
            z -= 64
        elif pos1[0] > pos2[0] and pos1[1] < pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                return False
            x -= 64
            z += 64
        elif pos1[0] < pos2[0] and pos1[1] < pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                return False
            x += 64
            z += 64
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True
      return False


class King(Piece):
    def islegal(self, ex_board, pos1, pos2):
      if(abs(abs(pos1[0]) - abs(pos2[0])) == 64 or pos1[0] - pos2[0] == 0) and (abs(abs(pos1[1]) - abs(pos2[1])) == 64 or pos1[1] - pos2[1] == 0) and pos1 != pos2:
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True
      return False

class Queen(Piece):
    def islegal(self, ex_board, pos1, pos2):             
      if abs(pos2[0] - pos1[0]) == abs(pos2[1] - pos1[1]) and pos2[0] != pos1[0]:
        if pos1[0] > pos2[0] and pos1[1] > pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                return False
            x -= 64
            z -= 64
        elif pos1[0] < pos2[0] and pos1[1] > pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                return False
            x += 64
            z -= 64
        elif pos1[0] > pos2[0] and pos1[1] < pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                return False
            x -= 64
            z += 64
        elif pos1[0] < pos2[0] and pos1[1] < pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                return False
            x += 64
            z += 64
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True
      elif(pos1[0] < pos2[0]) and (pos2[1] == pos1[1]):
        # finds pieces                         
        for c in ex_board:
            if c.loc[1] == pos2[1] and pos1[0] < c.loc[0] < pos2[0]:
              return False
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True
      elif(pos2[0] < pos1[0]) and (pos2[1] == pos1[1]):
        # finds pieces                 
        for c in ex_board:
            if (c.loc[1] == pos2[1]) and (pos1[0] > c.loc[0] > pos2[0]):
              return False
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True
      elif(pos1[0] == pos2[0]) and (pos2[1] > pos1[1]):
        # finds pieces                     
        for c in ex_board:
            if c.loc[0] == pos2[0] and pos1[1] < c.loc[1] < pos2[1]:
              return False
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True
      elif(pos1[0] == pos2[0]) and (pos2[1] < pos1[1]):
        # finds pieces                     
        for c in ex_board:
            if c.loc[0] == pos2[0] and pos1[1] > c.loc[1] > pos2[1]:
              return False
        for c in ex_board:
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team:
              return False
            else:
              ex_board.pop(ex_board.index(c))
              return True
        return True 
      return False   


class Elephant(Piece):
    def islegal(self, ex_board, pos1, pos2):   
      if((abs(pos1[0] - pos2[0]) == 128) and (abs(pos2[1] - pos1[1]) == (128))):
        if pos1[0] > pos2[0] and pos1[1] > pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                c.image = 'Explosion.png'
                drawpieces(ex_board)
                time.sleep(.25)
                ex_board.pop(c)
                drawpieces(ex_board)
                return True
            x -= 64
            z -= 64
        elif pos1[0] < pos2[0] and pos1[1] > pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                c.image = 'Explosion.png'
                drawpieces(ex_board)
                time.sleep(.25)
                ex_board.pop(c)
                drawpieces(ex_board)
                return True
            x += 64
            z -= 64
        elif pos1[0] > pos2[0] and pos1[1] < pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                c.image = 'Explosion.png'
                drawpieces(ex_board)
                time.sleep(.25)              
                ex_board.pop(c)
                drawpieces(ex_board)
                return True
            x -= 64
            z += 64
        elif pos1[0] < pos2[0] and pos1[1] < pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                c.image = 'Explosion.png'
                drawpieces(ex_board)
                time.sleep(.25)
                ex_board.pop(c)
                drawpieces(ex_board)               
                return True
            x += 64
            z += 64
        for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                c.image = 'Explosion.png'
                drawpieces(ex_board)
                time.sleep(.25)
                ex_board.pop(c)
                drawpieces(ex_board)               
                return True

        return True
      return False  
      


class Pawn(Piece):
  def islegal(self, ex_board, pos1, pos2):              
    if self.team == 'g':
      if pos1[1] == 64:
        if ((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (128)) and (pos2[1] - pos1[1] > 0)):
          for c in ex_board:
            if c.loc == (pos1[0], 384):
              return False
          return True
      if((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (64)) and (pos2[1] - pos1[1] > 0)):
        return True
      elif (((pos1[0] - pos2[0] == 64) or (pos1[0] - pos2[0] == (-64))) and (pos2[1] - pos1[1]) == (64) and pos2[1] - pos1[1] > 0):
          for c in ex_board:
            if c.loc == (pos2[0], pos2[1]) and c.team == 'r':
              ex_board.pop((ex_board.index(c)))
              return True
    else:
      if pos1[1] == 448:
        #this is the only part that works
        if ((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (-128)) and (pos2[1] - pos1[1] < 0)):
          for c in ex_board:
            if c.loc == (pos1[0], 384):
              return False
          return True
      if((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (-64)) and (pos2[1] - pos1[1] < 0)):
        return True
      elif (((pos1[0] - pos2[0] == 64) or (pos1[0] - pos2[0] == (-64))) and (pos2[1] - pos1[1]) == (-64) and pos2[1] - pos1[1] < 0):
          for c in ex_board:
            if c.loc == (pos2[0], pos2[1]) and c.team == 'g':
              ex_board.pop((ex_board.index(c)))
              return True
    return False

 
#Assiging places 
        
gR1 = Rook('', '', '', (0,0))
gN1 = Knight('', '', '', (0,0))
gB1 = Boat('', '', '', (0,0))
gE = Elephant('', '', '', (0,0)) 
gK = King('', '', '', (0,0))
gQ = Queen('', '', '', (0,0))
gB2= Boat('', '', '', (0,0))
gN2 = Knight('', '', '', (0,0))
gR2 = Rook('', '', '', (0,0))
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
rR1 = Rook('', '', '', (0,0))
rB1 = Boat('', '', '', (0,0))
rN1 = Knight('', '', '', (0,0))
rE = Elephant('', '', '', (0,0))
rK = King('', '', '', (0,0))
rQ = Queen('', '', '', (0,0))
rB2 = Boat('', '', '', (0,0))
rN2 = Knight('', '', '', (0,0))
rR2 = Rook('', '', '', (0,0))

Pieces = [gR1, gN1, gB1, gE, gK, gQ, gB2, gN2, gR2, gP1, gP2, gP3, gP4, gP5, gP6, gP7, gP8, gP9, rP1,rP2,rP3,rP4,rP5,rP6,rP7,rP8,rP9,rR1,rN1,rB1,rE,rQ,rK,rB2,rN2,rR2]
def drawboard(screen):
  colors=[pygame.Color('green'),pygame.Color('red')]
  for r in range(9):
      for c in range(9):
        color=colors[(r+c)%2]
        pygame.draw.rect(screen, color, pygame.Rect(c*64,r*64,64,64))
  


pieces_names = ["Rook", "Knight", "Boat", "Elephant", "King", "Queen", "Boat", "Knight", "Rook"]

#putting pieces in board with for loop. '_' is an unoccupied space
for i in range(0, 80):
  if i < 9:
    Pieces[i] = Pieces[i].__class__("g", pieces_names[i],('assets/Green_' + pieces_names[i]+ '.png'), ((64*i), 0))
  elif 8 < i < 18:
   Pieces[i] = Pawn("g", 'Pawn',('assets/Green_Pawn.png'), ((64*(i-9), 64)))
  elif 17 < i  < 27:
    Pieces[i] = Pawn('r', 'Pawn', ('assets/Red_Pawn.png'), ((64*(i-18)), 64*7))
  elif 26 < i < 36:
    Pieces[i] = Pieces[i].__class__('r', pieces_names[(i-27)], ('assets/Red_' + pieces_names[i-27]+'.png'), ((64*(i-27), 64*8)))



#putting board into the game
def drawpieces(ex_board):
  for i in ex_board:
    screen.blit(pygame.image.load(i.image), (i.loc))
#Getting tupple mouse click positions
def read_pos(stri):
  stri = stri.split(',')
  return(int(stri[0]), int(stri[1]))

#creating the turn logic 
move = 0
def isturn(piece, turn):
  if turn % 2 == 0 and piece.team == 'r':
    return True
  elif turn % 2 != 0 and piece.team == 'g':
    return True
  else:
    return False

pygame.display.flip()

#Assigning positions for the mouse clicks using placeholder values (-1,-1) cannot be clicked
pos1 = [-1,-1]
pos2 = [-1, -1]
running = True

while running:
  #sending is a variable with all of the pieces in toString format.
  sending = ''
  for i in Pieces:
    sending+= i.toString()
  n = Network()
  n.send(sending)
#I'm messing around to make the network work
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    #Recognizing first and second clicks
  if n.connect() != None:
    if read_pos(n.connect()) != (-1, -1):  
      if pos1 == [-1,-1]:
        pos1 = read_pos(n.connect())
        pos1 = [(pos1[0] - (int(pos1[0]) % 64)), pos1[1] - pos1[1] % 64]
        pos2 = [-1,-1]
      elif pos1 != [-1, -1]:
        read_pos(n.connect())
        pos2 = [(pos2[0] - pos2[0] % 64), (pos2[1] - pos2[1] % 64)] 
        for i in Pieces:
          if (i.loc == (pos1[0], pos1[1])):      
            if isturn(i, move) and i.islegal(Pieces, pos1, pos2):
              move += 1            
              i.loc = (pos2[0], pos2[1])

            
            pos1 = [-1,-1]
  
  #marking pieces 
  
  
  

  
  
  

  drawpieces(Pieces)


  pygame.display.update()