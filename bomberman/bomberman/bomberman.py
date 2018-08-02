
from pygame import *
import numpy as np

FPS = 100
HEIGHT = 840
WIDTH = 1024
TITLE = "BomberMan"

class Bomb(object):
    def __init__(self,x,y):
        self.rect = Rect(x-15,y-15,30,30)
    def draw(self,screen):
        draw.rect(screen,(0,200,0),self.rect,1)

class Player(object):
    def __init__(self,x=0,y=0):
        self.rect = Rect(x-15,y-15,30,30)
    
    def draw(self,screen):
        draw.rect(screen,(200,0,0),self.rect,1)
    
    def move(self,x,y,board):
        self.rect.x += x
        self.rect.y += y

        for rect in board.rects:
            if self.rect.colliderect(rect):
                self.rect.x -= x
                self.rect.y -= y               

    def dropBomb(self,board,player):
        board.bombs.append(Bomb(player.rect.x,player.rect.y))

class Block(Rect):
    color = (200,200,200)

class Wall(Rect):
    color = (100,100,100)

class Board():
    def __init__(self):
        self.rects = []

        file = open("maps/map1.dat")
        self.size = HEIGHT/17
        marginLeft = self.size
        marginTop = self.size
        i = 0
        for line in file:
            for j in range(len(line)):
                if line[j] == "#":
                    self.rects.append(Block(marginLeft+i*self.size,marginTop+j*self.size,self.size-1, self.size -1 ))
            i += 1
        for j in range(-1,i+1):
            self.rects.append(Wall(marginLeft-self.size,marginTop+j*self.size,self.size-1, self.size -1 ))
            self.rects.append(Wall(marginLeft+15.*self.size,marginTop+j*self.size,self.size-1, self.size -1 ))
        for j in range(i):
            self.rects.append(Wall(marginLeft+j*self.size,marginTop-self.size,self.size-1, self.size -1 ))
            self.rects.append(Wall(marginLeft+j*self.size,marginTop+15*self.size,self.size-1, self.size -1 ))

        self.bombs = []

    def draw(self,screen):
        for rect in self.rects:
            draw.rect(screen,rect.color,rect,0)
        for bomb in self.bombs:
            bomb.draw(screen)

class Game(object):
    def __init__(self):
        init()
        display.set_caption(TITLE)
        self.screen = display.set_mode((WIDTH,HEIGHT))
        self.clock = time.Clock()

        self.board = Board()
        self.player1 = Player(70,70)

    def draw(self):
        self.screen.fill( (0,0,0) )
        self.board.draw(self.screen)
        self.player1.draw(self.screen)

    def update(self):
        #print ("hej")
        self.draw()
        self.clock.tick(FPS)
        display.flip()



def main():
    endProgram = False
    game = Game()
    while not endProgram:
        for ev in event.get():
            if ev.type == QUIT:
                endProgram = True    
        game.update()
        keys=key.get_pressed()
        if keys[K_UP]:
            game.player1.move(0,-1,game.board)
        if keys[K_DOWN]:
            game.player1.move(0,1,game.board)
        if keys[K_LEFT]:
            game.player1.move(-1,0,game.board)
        if keys[K_RIGHT]:
            game.player1.move(1,0,game.board)
        if keys[K_SPACE]:
            game.player1.dropBomb(game.board,game.player1)

if __name__=="__main__":
    main()