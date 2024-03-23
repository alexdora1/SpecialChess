import time
import socket
from _thread import *
#Adding a function to show the clicking

print('hello world')


clientNumber = 0
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
            if c.team == self.team or c.image == 'assets/Rock.png':
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
            if c.team == self.team or c.image == 'assets/Rock.png':
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
            if c.team == self.team or c.image == 'assets/Rock.png':
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
            if c.team == self.team or c.image == 'assets/Rock.png':
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
          #boats crash on rocks! 
          if c.image == 'assets/Rock.png':
            if abs(pos2[0] - c.loc[0]) <= 64 or abs(pos2[1] - c.loc[1]) <= 64:
              self.loc = (pos2[0], pos2[1])
              time.sleep(1)
              ex_board.pop(ex_board.index(self))
              time.sleep(.5)
              return False              
          if c.loc == (pos2[0], pos2[1]):
            if c.team == self.team or c.image == 'assets/Rock.png':
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
            if c.team == self.team or c.image == 'assets/Rock.png':
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
            if c.team == self.team or c.image == 'assets/Rock.png':
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
            if c.team == self.team or c.image == 'assets/Rock.png':
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
            if c.team == self.team or c.image == 'assets/Rock.png':
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
            if c.team == self.team or c.image == 'assets/Rock.png':
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
            if c.team == self.team or c.image == 'assets/Rock.png':
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
                c.image = 'assets/Explosion.png'
                time.sleep(1)
                ex_board.pop(ex_board.index(c))
                return True
            x -= 64
            z -= 64
        elif pos1[0] < pos2[0] and pos1[1] > pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                c.image = 'assets/Explosion.png'
                time.sleep(1)
                ex_board.pop(ex_board.index(c))
                return True
            x += 64
            z -= 64
        elif pos1[0] > pos2[0] and pos1[1] < pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                c.image = 'assets/Explosion.png'
                time.sleep(1)              
                ex_board.pop(ex_board.index(c))
                return True
            x -= 64
            z += 64
        elif pos1[0] < pos2[0] and pos1[1] < pos2[1]:
          x = pos1[0]
          z = pos1[1]
          while x != pos2[0]:
            for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                c.image = 'assets/Explosion.png'
                time.sleep(1)
                ex_board.pop(ex_board.index(c))             
                return True
            x += 64
            z += 64
        for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                c.image = 'assets/Explosion.png'
                time.sleep(.5)
                ex_board.pop(ex_board.index(c))          
                return True

        return True
      return False  
      


class Pawn(Piece):
  def islegal(self, ex_board, pos1, pos2):              
    if self.team == 'g':
      if pos1[1] == 64:
        if ((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (128)) and (pos2[1] - pos1[1] > 0)):
          for c in ex_board:
            if c.loc == (pos1[0], 128):
              return False
          return True
      if((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (64)) and (pos2[1] - pos1[1] > 0)):
        if pos2[1] == 512:
          self.image = 'assets/Rock.png' 
        return True
      elif (((pos1[0] - pos2[0] == 64) or (pos1[0] - pos2[0] == (-64))) and (pos2[1] - pos1[1]) == (64) and pos2[1] - pos1[1] > 0):
          for c in ex_board:
            if c.loc == (pos2[0], pos2[1]) and c.team == 'r':
              ex_board.pop((ex_board.index(c)))
              if pos2[1] == 512:
                self.image = 'assets/Rock.png' 
              return True
    else:
      if pos1[1] == 448:
        #this is the only part that works
        if ((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (-128)) and (pos2[1] - pos1[1] < 0)):
          for c in ex_board:
            if c.loc == (pos1[0], 0):
              return False
          return True
      if((pos1[0] - pos2[0] == 0) and ((pos2[1] - pos1[1]) == (-64)) and (pos2[1] - pos1[1] < 0)):
        for c in ex_board:
            if c.loc == (pos2[0], pos2[1]):
              return False
        if pos2[1] == 0:
                self.image = 'assets/Rock.png' 
        return True
      elif (((pos1[0] - pos2[0] == 64) or (pos1[0] - pos2[0] == (-64))) and (pos2[1] - pos1[1]) == (-64) and pos2[1] - pos1[1] < 0):
          for c in ex_board:
            if c.loc == (pos2[0], pos2[1]) and c.team == 'g':
              ex_board.pop((ex_board.index(c)))
              if pos2[1] == 0:
                self.image = 'assets/Rock.png'
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

#Getting tupple mouse click positions
def read_pos(str):
  str = str.split(',')
  return(int(str[0]), int(str[1]))

#creating the turn logic 
move = 0
def isturn(piece, turn):
  if turn % 2 == 0 and piece.team == 'r':
    return True
  elif turn % 2 != 0 and piece.team == 'g':
    return True
  else:
    return False



#Assigning positions for the mouse clicks using placeholder values (-1,-1) cannot be clicked
def Main(n):
  pos1 = [-1,-1]
  pos2 = [-1, -1]

    #sending is a variable with all of the pieces in toString format.
  sending = ''
  for i in Pieces:
    sending+= i.toString()
  n.send(sending)
#I'm messing around to make the network work
    #Recognizing first and second clicks
  if n.getPos() != None: 
    if read_pos(n.getPos()) != (-1, -1):  
      if pos1 == [-1,-1]:
        pos1 = read_pos(n.getpos())
        pos1 = [(pos1[0] - (int(pos1[0]) % 64)), pos1[1] - pos1[1] % 64]
        pos2 = [-1,-1]
      elif pos1 != [-1, -1]:
        read_pos(n.getpos())
        pos2 = [(pos2[0] - pos2[0] % 64), (pos2[1] - pos2[1] % 64)] 
        for i in Pieces:
          if (i.loc == (pos1[0], pos1[1])):      
            if isturn(i, move) and i.islegal(Pieces, pos1, pos2):
              move += 1            
              i.loc = (pos2[0], pos2[1])

            
            pos1 = [-1,-1]
  
  #marking pieces 
  
  
  

  
  
  
