import numpy as np
import random
HEIGHT=640
WIDTH=1024
TITLE="Mario"

mario=Actor("mario.png",(200,HEIGHT-100))
mario.vy=0
mario.time=0
mario.dir="right"
mario.dead=False


class Brick(Actor):
    def react(self):
        #print(mario.center[1]+mario.size[1]/2-obj.center[1]+obj.size[1]/2)
        if np.abs(mario.center[1]+mario.size[1]/2-self.center[1]+self.size[1]/2)<15: # z gory
            mario.vy = 0
            mario.bottom = self.top
        elif np.abs(mario.center[1]-mario.size[1]/2-self.center[1]-self.size[1]/2)<15: # z dolu
            mario.vy = 0
            mario.top = self.bottom
        elif np.abs(mario.center[0]+mario.size[0]/2-self.center[0]+self.size[0]/2)<15: # z prawej
            moveall(6)
        elif np.abs(mario.center[0]-mario.size[0]/2-self.center[0]-self.size[0]/2)<15: # z lewej
            moveall(-6)
    def move(self):
        pass


class Block(Actor):
    def react(self):
        #print(mario.center[1]+mario.size[1]/2-obj.center[1]+obj.size[1]/2)
        if np.abs(mario.center[1]+mario.size[1]/2-self.center[1]+self.size[1]/2)<15: # z gory
            mario.vy = 0
            mario.bottom = self.top
        elif np.abs(mario.center[1]-mario.size[1]/2-self.center[1]-self.size[1]/2)<15: # z dolu
            mario.vy = 0
            mario.top = self.bottom
            animate(self, pos=(self.center[0], -10000))
        elif np.abs(mario.center[0]+mario.size[0]/2-self.center[0]+self.size[0]/2)<15: # z prawej
            moveall(6)
        elif np.abs(mario.center[0]-mario.size[0]/2-self.center[0]-self.size[0]/2)<15: # z lewej
            moveall(-6)
    def move(self):
        pass

class Cloud(Actor):
    def react(self):
        pass
    def move(self):
        self.x=(self.x-1)%7000

class Monster(Actor):
    def react(self):
        #print(mario.center[1]+mario.size[1]/2-obj.center[1]+obj.size[1]/2)
        if np.abs(mario.center[1]+mario.size[1]/2-self.center[1]+self.size[1]/2)<15: # z gory
            mario.vy = 0
            mario.bottom = self.top
            animate(self, pos=(self.right+50, HEIGHT+50))
            #animate(self, pos=(200, 100))

            #objs.remove(self)
        elif np.abs(mario.center[1]-mario.size[1]/2-self.center[1]-self.size[1]/2)<15: # z dolu
            mario.vy = 0
            mario.top = self.bottom
        elif np.abs(mario.center[0]+mario.size[0]/2-self.center[0]+self.size[0]/2)<15: # z prawej
            mario.dead = True
            newgame()
        elif np.abs(mario.center[0]-mario.size[0]/2-self.center[0]-self.size[0]/2)<15: # z lewej
            mario.dead = True
            newgame()

    def move(self):
        for obj in objs:
            if obj!=self and self.colliderect(obj) and not obj.image in ["bush.png","brick.png","hill.png"]:
                self.dir=-self.dir

        self.x=self.x+self.dir

class Bush(Actor):
    def react(self):
        pass
    def move(self):
        pass

objs = []


for i in range(200):
    objs.append(Brick("brick.png",(i*32,HEIGHT-18)))
    objs.append(Brick("brick.png",(i*32,HEIGHT-50)))
for i in [35,35,35,35,35,34]:
    objs.remove(objs[i])
#objs.append(Brick("brick.png",(7*32,HEIGHT-182)))
for i in range(5):
    for j in range(i):
        objs.append(Brick("brick2.png",(i*32+12*32,HEIGHT-82-j*32)))
        objs.append(Brick("brick2.png",((5-i)*32+19*32,HEIGHT-82-j*32)))
objs.append(Brick("brick2.png",(27*32+12*32,HEIGHT-82-3*32)))
objs.append(Brick("brick2.png",(28*32+12*32,HEIGHT-82-3*32)))
objs.append(Brick("brick2.png",(31*32+12*32,HEIGHT-82-3*32)))
objs.append(Brick("brick2.png",(32*32+12*32,HEIGHT-82-3*32)))
objs.append(Brick("brick2.png",(32*32+12*32,HEIGHT-82-3*32)))
for i in [73,73,73,73,73,73,73,73,73,73,73,72]:
    objs.remove(objs[i])


for i in range (18):
    objs.append(Cloud("cloud.png",(i*12*32,HEIGHT-random.randint(300,650))))

for i in range (9):
    objs.append(Bush("bush.png",(i*26*32+30,HEIGHT-94)))

for i in range (9):
    objs.append(Bush("hill.png",(i*35*32-12,HEIGHT-104)))


objs.append(Monster("enemy1.png",(25*32-12,HEIGHT-82)))
objs[-1].dir = 1

objs.append(Brick("brick2.png",(33*32-12,HEIGHT-82)))

objs.append(Block("block.png",(7*32+1,HEIGHT-182)))
objs.append(Block("block.png",(8*32+1,HEIGHT-182)))
objs.append(Block("block.png",(9*32+1,HEIGHT-182)))
objs.append(Block("block.png",(10*32+1,HEIGHT-182)))

####################################################

for obj in objs:
    obj.oldpos=obj.pos

def newgame():
    mario.pos = (200,HEIGHT-250)
    mario.vy=0
    mario.time=0
    mario.dir="right"
    mario.dead=False
    
    for obj in objs:
        obj.pos=obj.oldpos
    
#newgame()



def draw():
    screen.fill((148, 146, 255))
    for obj in objs:
        obj.draw()
    mario.draw()


def moveall(x):
    if x>0:
        if 0<=mario.x:
            mario.x=mario.x-x
        elif mario.x<0:
            mario.x=0
    else:
        if 0<=mario.x<WIDTH/2:
            mario.x=mario.x-x
        elif mario.x>WIDTH/2:
            mario.x=WIDTH/2
        elif mario.x>=WIDTH/2:
            for obj in objs:
                obj.x=obj.x+x            


def move(dt):
    
    if mario.dir=="right":
        mario.image="mario.png"
    else:
        mario.image="marioleft.png"
     
    uy=mario.vy
    mario.vy=mario.vy+2000.0*dt
    mario.y=mario.y+(uy+mario.vy)*0.5*dt

    
    if keyboard.right:
        moveall(-2)
        mario.dir="right"
        if mario.time<8:
            mario.image="mariomove.png"
        else:
            mario.image="mariomove2.png"
    if keyboard.left:
        moveall(2)
        mario.dir="left"
        if mario.time<8:
            mario.image="mariomoveleft.png"
        else:
            mario.image="mariomoveleft2.png"
    
    for obj in objs:
        if  mario.colliderect(obj):
            obj.react()

   
    if mario.vy !=0 and mario.dir=="right":
        mario.image="mariojump.png"
    elif mario.vy !=0 and mario.dir=="left":
        mario.image="mariojumpleft.png"
    
    if mario.bottom>HEIGHT:
        mario.dead = True

def update(dt):
    mario.time=(mario.time+1)%16
    move(dt)
    for obj in objs:
        obj.move()
    if mario.dead:
        print("Umarles")
        newgame()

def on_key_down(key):
    if key==keys.SPACE and mario.vy==0:
        mario.vy=-800