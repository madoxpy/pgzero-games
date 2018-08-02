HEIGHT=850
WIDTH=850
TITLE="Bomberman"
import random
from pygame import *

class Block(Actor):
    def update(self,p1,p2):
        pass

class Brick(Actor):
    def update(self,p1,p2):
        pass

class Player1(Actor):
    health = 3
    clock = 0
    absclock = 0
    nbomb = 1
    bombs=[]
    lastbombtime = 0
    radius = 1

    def update(self):
        self.clock=(self.clock+1)%60
        self.absclock=self.absclock+1

        for bomb in self.bombs:
            bomb.update()

    def move(self,x,y):
        self.x=self.x+x
        self.y=self.y+y

        if y>0 and x==0:
            self.image = str(int(self.clock/20)+1)+"player1down.png"
        if y<0 and x==0:
            self.image = str(int(self.clock/20)+1)+"player1up.png"
        if y==0 and x>0:
            self.image = str(int(self.clock/20)+1)+"player1right.png"
        if y==0 and x<0:
            self.image = str(int(self.clock/20)+1)+"player1left.png"

        for obj in objs:
            if self.colliderect(obj) and obj.__class__.__name__ in ["Block","Brick"]:
                self.x=self.x-x
                self.y=self.y-y
                break 
    def plantbomb(self):
        x=int(self.center[0]/50)*50
        y=int(self.center[1]/50)*50
        if len(self.bombs) < self.nbomb and self.absclock-self.lastbombtime>10:
            self.bombs.append(Bomb1("bomb1.png",topleft=(x,y))) 
            self.lastbombtime=self.absclock

class Bomb1(Actor):
    clock = 5 

    def detonate(self):
        objs.append(Fire("fire1.png",topleft=self.topleft))
        for k in [[0,1],[0,-1],[1,0],[-1,0]]:
            for i in range(1,player1.radius+1):  
                objs.append(Fire("fire1.png",topleft=(self.topleft[0]+50*i*k[0],self.topleft[1]+50*i*k[1])))
                done = False
                for obj in objs[0:-1]:
                    if objs[-1].colliderect(obj) and obj.__class__.__name__=="Brick":
                        done = True
                if done:
                    break  
        player1.bombs.remove(self)
      
    def update(self):
        self.clock=self.clock-0.07
        if int(self.clock)+1>0:
            self.image="bomb"+str(int(self.clock)+1) +".png"

            for obj in objs:
                if self.colliderect(obj) and obj.__class__.__name__ == "Fire":
                    self.detonate()
                    break
        else:
            self.detonate()




class Player2(Actor):
    health = 3
    clock = 0
    absclock = 0
    nbomb = 1
    bombs=[]
    lastbombtime = 0
    radius = 1

    def update(self):
        self.clock=(self.clock+1)%60
        self.absclock=self.absclock+1

        for bomb in self.bombs:
            bomb.update()

    def move(self,x,y):
        self.x=self.x+x
        self.y=self.y+y

        if y>0 and x==0:
            self.image = str(int(self.clock/20)+1)+"player2down.png"
        if y<0 and x==0:
            self.image = str(int(self.clock/20)+1)+"player2up.png"
        if y==0 and x>0:
            self.image = str(int(self.clock/20)+1)+"player2right.png"
        if y==0 and x<0:
            self.image = str(int(self.clock/20)+1)+"player2left.png"

        for obj in objs:
            if self.colliderect(obj) and obj.__class__.__name__ in ["Block","Brick"]:
                self.x=self.x-x
                self.y=self.y-y
                break 
    def plantbomb(self):
        x=int(self.center[0]/50)*50
        y=int(self.center[1]/50)*50
        if len(self.bombs) < self.nbomb and self.absclock-self.lastbombtime>10:
            self.bombs.append(Bomb2("bomb1.png",topleft=(x,y))) 
            self.lastbombtime=self.absclock

class Bomb2(Actor):
    clock = 5 

    def detonate(self):
        objs.append(Fire("fire1.png",topleft=self.topleft))
        for k in [[0,1],[0,-1],[1,0],[-1,0]]:
            for i in range(1,player1.radius+1):  
                objs.append(Fire("fire1.png",topleft=(self.topleft[0]+50*i*k[0],self.topleft[1]+50*i*k[1])))
                done = False
                for obj in objs[0:-1]:
                    if objs[-1].colliderect(obj) and obj.__class__.__name__=="Brick":
                        done = True
                if done:
                    break  
        player2.bombs.remove(self)
      
    def update(self):
        self.clock=self.clock-0.07
        if int(self.clock)+1>0:
            self.image="bomb"+str(int(self.clock)+1) +".png"

            for obj in objs:
                if self.colliderect(obj) and obj.__class__.__name__ == "Fire":
                    self.detonate()
                    break
        else:
            self.detonate()

class Fire(Actor):
    clock = 3
    def update(self,p1,p2):
        self.clock=self.clock-0.1
        if int(self.clock)+1>0:
            self.image="fire"+str(int(self.clock)+1) +".png"
        else:
            if self.colliderect(p1):
                p1.center=(75,75)
                p1.health=p1.health-1
            if self.colliderect(p2):
                p2.center=(WIDTH-75,HEIGHT-75)
                p2.health=p2.health-1
            for obj in objs:
                if self.colliderect(obj) and obj.__class__.__name__ != "Block":
                    if random.random()<0.03 and obj.__class__.__name__ == "Brick":
                        objs.append(Bonus1("bonus1.png",topleft=obj.topleft))
                    elif random.random()<0.03 and obj.__class__.__name__ == "Brick":
                        objs.append(Bonus2("player1hearth.png",topleft=obj.topleft))
                    elif random.random()<0.03 and obj.__class__.__name__ == "Brick":
                        objs.append(Bonus3("bonus3.png",topleft=obj.topleft))                    
                    objs.remove(obj)
                    break
            
            #objs.remove(self)    
class Bonus1(Actor): # radius
    def update(self,p1,p2):
        if p1.colliderect(self):
            p1.radius=p1.radius+1
            if p1.radius > 5:
                p1.radius = 5
            objs.remove(self) 
        elif p2.colliderect(self):
            p2.radius=p2.radius+1
            if p2.radius > 5:
                p2.radius = 5
            objs.remove(self)       
class Bonus2(Actor): #health
    def update(self,p1,p2):
        if p1.colliderect(self):
            p1.health=p1.health+1
            if p1.health > 7:
                p1.health = 7
            objs.remove(self) 
        elif p2.colliderect(self):
            p2.health=p2.health+1
            if p2.health > 7:
                p2.health = 7
            objs.remove(self)   
class Bonus3(Actor): # nbomb
    def update(self,p1,p2):
        if p1.colliderect(self):
            p1.nbomb=p1.nbomb+1
            if p1.nbomb > 5:
                p1.nbomb = 5
            objs.remove(self) 
        elif p2.colliderect(self):
            p2.nbomb=p2.nbomb+1
            if p2.nbomb > 5:
                p2.nbomb = 5
            objs.remove(self)               

def newgame():
    for i in range(17):
        objs.append(Block("block.png",topleft=(i*50,0)))
        objs.append(Block("block.png",topleft=(i*50,HEIGHT-50)))
    for i in range(15):
        objs.append(Block("block.png",topleft=(0,i*50+50)))
        objs.append(Block("block.png",topleft=(WIDTH-50,i*50+50)))

    file=open("map1.dat")

    i=1
    for line in file:
        for j in range(len(line)):
            if line[j]=="#":
                objs.append(Brick("brick.png",topleft=(i*50,j*50+50)))
        i=i+1


    # create blocks around board
    # load map from map1.EI


def draw():
    screen.fill((148, 146, 255))

    if player1.health>0 and player2.health>0:
        for obj in objs:
            obj.draw()
        player1.draw()
        for bomb in player1.bombs:
            bomb.draw()
        player2.draw()
        for bomb in player2.bombs:
            bomb.draw()

        for i in range(player1.health):
            screen.blit("player1hearth.png",(i*50,HEIGHT-50))
        for i in range(player2.health):
            screen.blit("player2hearth.png",(WIDTH-i*50-50,HEIGHT-50))
    else:
        if player1.health > player2.health:
            screen.draw.text("Player 1 win",color="black",midtop=(WIDTH//2,200),fontsize=70)
        elif player1.health < player2.health:
            screen.draw.text("Player 2 win",color="black",midtop=(WIDTH//2,200),fontsize=70)
        else:
            screen.draw.text("Draw",color="black",midtop=(WIDTH//2,200),fontsize=70)
def update():
    # updates of the clocks
    # players control
    speed = 2.5



    if keyboard.w:
        player1.move(0,-speed)
    if keyboard.s:
        player1.move(0,speed)
    if keyboard.a:
        player1.move(-speed,0)
    if keyboard.d:
        player1.move(speed,0)
    if keyboard.space:
            player1.plantbomb()

    if keyboard.up:
        player2.move(0,-speed)
    if keyboard.down:
        player2.move(0,speed)
    if keyboard.left:
        player2.move(-speed,0)
    if keyboard.right:
        player2.move(speed,0)
    if keyboard.rshift:
        player2.plantbomb()


    for obj in objs:
        obj.update(player1,player2)
    player1.update()
    player2.update()
 
objs = []
newgame()
player1 = Player1("2player1down.png",(75,75))
player2 = Player2("2player2down.png",(WIDTH-75,HEIGHT-75))
