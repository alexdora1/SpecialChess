import pygame
import time
import socket
import threading 
#Adding a function to show the clicking
pygame.font.init()

(width, height) = (575, 575)
screen = pygame.display.set_mode((width, height))




Display_Name = 'Special Chess'
pygame.display.set_caption(Display_Name)

class Piece:
    def __init__(self, team, type, image, loc):
        self.team = team
        self.type = type
        self.image = image
        self.loc = loc
    def islegal(self, ex_board, pos1,pos2):
      print("We're in the piece")
      return True


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
              drawpieces(ex_board)
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
                drawpieces(ex_board)
                time.sleep(1)
                ex_board.pop(ex_board.index(c))
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
                c.image = 'assets/Explosion.png'
                drawpieces(ex_board)
                time.sleep(1)
                ex_board.pop(ex_board.index(c))
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
                c.image = 'assets/Explosion.png'
                drawpieces(ex_board)
                time.sleep(1)              
                ex_board.pop(ex_board.index(c))
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
                c.image = 'assets/Explosion.png'
                drawpieces(ex_board)
                time.sleep(1)
                ex_board.pop(ex_board.index(c))
                drawpieces(ex_board)               
                return True
            x += 64
            z += 64
        for c in ex_board:
              if c.loc == (x,z) and c.loc != self.loc:
                c.image = 'assets/Explosion.png'
                drawpieces(ex_board)
                time.sleep(.5)
                ex_board.pop(ex_board.index(c))
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

#Alex: I know this isn't pretty, but this is the best way to have it work with multiplayer
global Pieces
  

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

#ultraPieces is the list for the pieces that automatically kill the thing
global ultraPieces
ultraPieces = []

def drawboard(screen):
  Piecewidth = 64 
  Pieceheight = 64

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

#putting the name text in there
def drawtext(text):
  baseFont = pygame.font.SysFont('Comic Sans MS', 20)
  textSurface = baseFont.render(text, False, (0,0,255))
  screen.blit(textSurface, (50,250))


#creating the turn logic 
move = 0
def isturn(piece, turn):
  if turn % 2 == 0 and piece.team == 'r':
    return True
  elif turn % 2 != 0 and piece.team == 'g':
    return True
  else:
    return False
#We're going to use this to determine which team the player is on -- the server already sends it

compteam = 'null'

def recieved(conn):
  global compteam
  global move
  global player_names
  global ultraPieces
  while compteam == 'null':
    data = conn.recv(100)  # Receive data from the client
    if not data:
        break
    if '*' in data.decode():     
      data = data.decode()
      dataList = data.split('*')
      compteam = dataList[1]
      if len(dataList) > 2:
        player_names = dataList[2]
  while True:
    data = conn.recv(100)  # Receive data from the client
    if not data:
        break
    if '#' in data.decode() and '(self' not in data.decode():
      #splitting something in the form of g(0, 128)[0, 128] in order to move a piece
      data = data.decode()
      data = data.split('#')
      initialLoc = (int(data[0]), int(data[1]))
      finalLoc = (int(data[2]), int(data[3]))
      for i in Pieces:
        if i.loc == initialLoc and i.islegal(Pieces, initialLoc, finalLoc):
          i.loc == finalLoc
          move += 1
          break

      for i in Pieces:
        if i.loc == initialLoc:
          i.loc = finalLoc
    elif '(self' in data.decode() and player_names == 'w':
      #setting display name      
      player_names = data.decode()
      print('player names:', player_names)
    elif 'Ultra^' in data.decode():
      #getting the ultra pieces
      data = data.decode()
      dataList = data.split('^')
      firstUltra = dataList[1]
      firstUltra = int(firstUltra)
      secondUltra = dataList[3]
      secondUltra = int(secondUltra)
      ultraPieces.append(Pieces[firstUltra])
      ultraPieces.append(Pieces[secondUltra])
      if compteam == 'r':
        location = Pieces[secondUltra].loc()
        ##pygame.draw.rect(screen, color, pygame.Rect(c*64,r*64,64,64))
        pygame.draw.rect(screen, (255,192,203), pygame.Rect(location[0], location[1], 64, 64))
      elif compteam == 'g':
        location = Pieces[firstUltra].loc()
        pygame.draw.rect(screen, (255,192,203), pygame.Rect(location[0], location[1], 64, 64))

    elif 'BYEBYEBYEBYEBYEBYEBYE' in data.decode():
      print('Opponent quit')
      global running
      running = False

          



pygame.display.flip()

#Assigning positions for the mouse clicks using placeholder values (-1,-1) cannot be clicked

pos1 = [-1,-1]
pos2 = [-1, -1]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#GFS IP on the one below this
mysock.connect(('172.27.8.183', 5555))
#mysock.connect(('192.168.1.205', 5555))
global player_names
player_names = 'w'
recieved_thread = threading.Thread(target=recieved, args=(mysock,), daemon = True)
recieved_thread.start()
running = True
#Clicking rect is the rectangle that tells a student where they are clicking 
rectColor = (255,165,0)
rectSquare = (0, 0, 0, 0)



while running:
  #pygame.draw.rect(screen, color, pygame.Rect(c*64,r*64,64,64))
  
  drawboard(screen)
  pygame.draw.rect(screen, rectColor, pygame.Rect(rectSquare))
  drawpieces(Pieces)
  drawtext(player_names)


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    #Recognizing first and second clicks 
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if pos1 == [-1,-1]:
        pos1 = pygame.mouse.get_pos()
        pos1 = [(pos1[0] - (int(pos1[0]) % 64)), pos1[1] - pos1[1] % 64]
        rectColor = (255,165,0)
        rectSquare = (pos1[0], pos1[1], 64, 64)

        
        pos2 = [-1,-1]
      elif pos1 != [-1, -1]:
        pos2 = pygame.mouse.get_pos()
        pos2 = [(pos2[0] - pos2[0] % 64), (pos2[1] - pos2[1] % 64)] 
        rectSquare = (pos2[0], pos2[1], 64, 64)
        rectColor = (255,223,0)
      

        for i in Pieces:
          if (i.loc == (pos1[0], pos1[1])):      
            if i.team == compteam and isturn(i, move) and i.islegal(Pieces, pos1, pos2):              
              try:
                sending = str(i.loc[0]) + '#' + str(i.loc[1]) + '#' + str(pos2[0]) + '#' + str(pos2[1])
                sending = sending.encode()
                sent_bytes = 0
                while sent_bytes < len(sending):
                    
                    sent = mysock.send(sending[sent_bytes:])
                    if sent == 0:
                        print('Socket connection broken')
                        raise RuntimeError("Socket connection broken")

                    sent_bytes += sent                 
              except socket.timeout:
                  print('Timeout error')
                  
                  mysock.connect()
              except socket.error as e:
                  print('Socket error:', e)
              
              move += 1            
              pygame.draw.rect(screen, pygame.Color('blue'), pygame.Rect((pos1[0] - ((pos1[0]) % 64)), (pos1[1]-(pos1[1]%64)), 64, 64))
              i.loc = (pos2[0], pos2[1])
              pygame.draw.rect(screen, pygame.Color('purple'), pygame.Rect((pos2[0] - (pos2[0]) % 64), (pos2[1]-pos2[1]%64), 64, 64))
              drawpieces(Pieces)

        
        pos1 = [-1,-1]
  
  #marking pieces 
  
  
  

  
  
  

  drawpieces(Pieces)


  pygame.display.update()
sending = 'BYEBYEBYEBYEBYEBYEBYE'
mysock.send(sending.encode())
mysock.close()
