import time
import chess
import pygame
from init import drawimages, loadimages, drawboard, drawmarker


def calculateFen(board):
    fen=board.fen()

    for i in fen:
        if i.isdigit():
            fen = fen.replace(i, '*' * int(i))
        elif i == "/":
            fen = fen.replace(i, '')

    fen=list(fen)
    a=list(fen[0:8])
    b=list(fen[8:16])
    c=list(fen[16:24])
    d=list(fen[24:32])
    e=list(fen[32:40])
    f=list(fen[40:48])
    g=list(fen[48:56])
    h=list(fen[56:64])

    fen=[a, b, c, d, e, f, g, h,]
    return fen


def move(board, move):
    try:
        board.push_san(move)
    except:
        pass
   
    return board


def main():
    initialSquare=''
    targetSquare=''

    numbersRow=['a','b','c','d','e','f','g','h']
    numbersCol=['8','7','6','5','4','3','2','1']

    colpos = 0
    rowpos = 0

    board=chess.Board()
    fen=calculateFen(board)

    #initialize pygame, assets
    pygame.init()
    screen = pygame.display.set_mode((512,512))
    clock=pygame.time.Clock()
    screen.fill(pygame.Color('White'))
    loadimages()
    
    #game loop
    while True:

        drawboard(screen)     
        drawmarker(screen, initialSquare, colpos, rowpos)
        drawimages(screen, calculateFen(board))


        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                quit()

            if board.is_checkmate():
                time.sleep(3)
                board = chess.Board()
            
            if i.type == pygame.MOUSEBUTTONDOWN:
                mousepos=pygame.mouse.get_pos()

                if mousepos[0]<513:
                    #calculate position of click, store x and y in colpos and rowpos
                    colpos=int(mousepos[1]/64)
                    rowpos=int(mousepos[0]/64)

                    #click on first square with a piece, store in firstinput
                    if initialSquare=='':
                        initialSquare=numbersRow[rowpos]+numbersCol[colpos]

                    #click on the destination sqaure, store in finalinput    
                    else:
                        targetSquare=initialSquare+numbersRow[rowpos]+numbersCol[colpos]
                        board=move(board, targetSquare) #if illegal move, move function passes

                        fen = calculateFen(board)
                        initialSquare=''
                        targetSquare=''
        
        pygame.display.flip()


if __name__ == "__main__":
    main()