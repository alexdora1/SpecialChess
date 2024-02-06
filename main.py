import pygame

(width, height) = (575, 575)
screen = pygame.display.set_mode((width, height))


colors=[pygame.Color('green'),pygame.Color('red')]
for r in range(9):
    for c in range(9):
      color=colors[(r+c)%2]
      pygame.draw.rect(screen, color, pygame.Rect(c*64,r*64,64,64))



pygame.display.set_caption('Special Chess')



pygame.display.flip()




running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False