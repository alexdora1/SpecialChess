import pygame

(width, height) = (575, 575)
screen = pygame.display.set_mode((width, height))

Piecewidth = 64 
Pieceheight = 64

colors=[pygame.Color('green'),pygame.Color('red')]
for r in range(9):
    for c in range(9):
      color=colors[(r+c)%2]
      pygame.draw.rect(screen, color, pygame.Rect(c*64,r*64,64,64))

pieces = ["Rook", "Knight", "Boat", "Elephant", "King", "Queen", "Boat", "Knight", "Rook"]


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

board = [a, b, c, d, e, f, g, h, i] 
#putting pieces in board with for loop. '_' is an unoccupied space
for i in range(0, 80):
  if i < 9:
    board[0].append('Green_' + pieces[i])

  elif 8 < i < 18:
    board[1].append('Green_Pawn')
  elif 17 < i  < 27:
    board[2].append('_')
  elif 26 < i < 36:
    board[3].append('_')
  elif 35 < i < 45:
    e.append('_')
  elif 44 < i < 54:
     f.append('_')
  elif 53 < i < 63:
     g.append('_')
  elif 62 < i < 72:
     h.append('Red_Pawn')
  elif 71< i:
      board[8].append('Red_' + pieces[(i-72)])
#Fixing an oopsie
board[8].append('Red_Rook')

#putting board into the game
def drawboard(ex_board):
  xloc = 0
  yloc = 0
  for i in ex_board:
    xloc = 0
    yloc += 64
    for z in i:
        if z != '_':
          screen.blit(pygame.image.load('assets/' + z + ".png"), (xloc, (yloc - 64)))
          xloc += 64


pygame.display.flip()




running = True
while running:
  drawboard(board)
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
  pygame.display.update()