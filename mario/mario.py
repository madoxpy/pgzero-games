import numpy as np
HEIGHT=640
WIDTH=1024
TITLE="Mario"

mario=Actor("mario.png",(200,HEIGHT-100))
mario.vy=0
mario.time=0
mario.dir="right"
mario.dead=False

bricks=[]
for i in range(250):
    bricks.append(Actor("brick.png",(i*32,HEIGHT-18)))
    bricks.append(Actor("brick.png",(i*32,HEIGHT-50)))

for i in [35,35,35,35,35,34]:
    bricks.remove(bricks[i])

objs = []
####################################################
# TU MOZNA TWORZYC NOWE PRZESZKODY
for i in range(5):
    for j in range(i):
        objs.append(Actor("brick.png",(i*32+12*32,HEIGHT-82-j*32)))
        objs.append(Actor("brick.png",((5-i)*32+19*32,HEIGHT-82-j*32)))

objs.append(Actor("brick.png",(27*32+12*32,HEIGHT-82-3*32)))
objs.append(Actor("brick.png",(28*32+12*32,HEIGHT-82-3*32)))
objs.append(Actor("brick.png",(31*32+12*32,HEIGHT-82-3*32)))
objs.append(Actor("brick.png",(32*32+12*32,HEIGHT-82-3*32)))

for i in [73,73,73,73,73,73,73,73,73,73,73,72]:
    bricks.remove(bricks[i])

####################################################
for brick in bricks:
    brick.oldpos=brick.pos
for obj in objs:
    obj.oldpos=obj.pos

def newgame():
    mario.pos = (200,HEIGHT-100)
    mario.vy=0
    mario.time=0
    mario.dir="right"
    mario.dead=False
    
    for brick in bricks:
        brick.pos=brick.oldpos
    for obj in objs:
        obj.pos=obj.oldpos
    
#newgame()



def draw():
    screen.fill((148, 146, 255))
    mario.draw()
    for brick in bricks:
        brick.draw()
    for obj in objs:
        obj.draw()

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
            for brick in bricks:
                brick.x=brick.x+x
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

    for brick in bricks:
        if mario.colliderect(brick):
            mario.y=HEIGHT-99
            mario.vy=0
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
            #print (obj.center[0]-16,mario.center[0],obj.center[0]+16)
            if mario.bottom > obj.top and obj.center[0]-32<mario.center[0]<obj.center[0]+32:
                #mario.y=mario.y-16
                mario.vy = 0
                mario.bottom = obj.top + 1
            else:
                if mario.x < obj.x:
                    moveall(6)
                if mario.x > obj.x:
                    moveall(-6)
            #mario.vy=0
            #mario.y=obj.top-60
    
    
    if mario.vy !=0 and mario.dir=="right":
        mario.image="mariojump.png"
    elif mario.vy !=0 and mario.dir=="left":
        mario.image="mariojumpleft.png"
    
    if mario.bottom>HEIGHT:
        mario.dead = True

def update(dt):
    mario.time=(mario.time+1)%16
    move(dt)
    if mario.dead:
        print("Umarles")
        newgame()

def on_key_down(key):
    if key==keys.SPACE and mario.vy==0:
        mario.vy=-800