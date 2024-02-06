import pygame

images={}
def loadimages():
    pieces=['wP','wN','wB','wR','wK','wQ','p','n','b','r','k','q']
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load('assets/' + piece + '.png'),(64,64))


def drawboard(screen):   
    colors=[pygame.Color('green'),pygame.Color('red')]
    for r in range(8):
        for c in range(8):
            color=colors[(r+c)%2]
            pygame.draw.rect(screen, color, pygame.Rect(c*64,r*64,64,64))


def drawimages(screen,board):
    for r in range(8):
        for c in range(8):
            piece=board[r][c]
            if piece!='*':
                if piece.isupper():
                    piece='w'+piece
                    screen.blit(images[piece], pygame.Rect(c*64,r*64,64,64))
                else:
                    screen.blit(images[piece], pygame.Rect(c*64,r*64,64,64))


def drawmarker(screen, initialSquare, colpos, rowpos):
    if initialSquare!='':
        for r in range(8):
            for c in range(8):
                if r==colpos and c==rowpos:
                    pygame.draw.rect(screen, pygame.Color('red'), pygame.Rect(c*64,r*64,64,64))