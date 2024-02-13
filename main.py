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
green_pieces = []
red_pieces = []
for i in pieces:
  green_pieces.append(pygame.image.load("assets/Green_" + i + ".png"))

for i in pieces: 
  red_pieces.append(pygame.image.load("assets/Red_" + i + ".png"))


for i in range (0,9):
    screen.blit(green_pieces[i], ((i*64),0))
    screen.blit(red_pieces[i], ((i*64, 512)))
    screen.blit(pygame.image.load('assets/Red_Pawn.png'), ((i*64), 448))
    screen.blit(pygame.image.load('assets/Green_Pawn.png'), (i*64, 64))



pygame.display.flip()




running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.update()