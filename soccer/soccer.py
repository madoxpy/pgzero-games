from pygame import time
from random import randint

HEIGHT=753
WIDTH=1200
TITLE="Soccer"
R = 30
V = 5

class Gate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = Rect(x,y,10,200)
        self.points = 0
    def draw(self):
        screen.draw.filled_rect(self.rect,(0,0,0))

    def update(self,ball):
        if self.x<ball.x<self.x+10 and self.y<ball.y<self.y+200:
            self.points = self.points + 1
            ball.x = WIDTH//2
            ball.y = HEIGHT//2
            ball.vx = randint(-4,4)
            ball.vy = randint(-4,4)
class Ball(object):
    def __init__(self):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.r = 20
        self.vx = -randint(-4,4)
        self.vy = randint(-4,4)
        self.color = (255,255,255)

    def draw(self):
        screen.draw.filled_circle((self.x,self.y), self.r, self.color)

    def update(self,p1,p2):
        if self.y-self.r<0 or self.y+self.r>HEIGHT:
            self.vy = -self.vy
        if self.x-self.r<0 or self.x+self.r>WIDTH:
            self.vx = -self.vx   

        for p in p1:
            if (p.x-self.x)**2+(p.y-self.y)**2<(p.r+self.r)**2:
                self.vy = -self.vy
                self.vx = -self.vx


        for p in p2:
            if (p.x-self.x)**2+(p.y-self.y)**2<(p.r+self.r)**2:
                self.vy = -self.vy
                self.vx = -self.vx

        self.x = self.x + self.vx
        self.y = self.y + self.vy

class Player(object):
    def __init__(self,x,y,color,downlimit=0,uplimit=0):
        self.x = x
        self.y = y
        self.r = R
        self.color = color
        self.active = False
        self.uplimit = uplimit
        self.downlimit = downlimit
    
    def draw(self):
        screen.draw.filled_circle((self.x,self.y), self.r, self.color)
        if self.active:
            screen.draw.circle((self.x,self.y), self.r-5, (255,255,255))
    
    def up(self):
        if self.y > self.uplimit:
            self.y = self.y - V

    def down(self):
        if self.y < self.downlimit:
            self.y = self.y + V

def draw():
    screen.blit("field.jpg",(0,0))
    gate1.draw()
    gate2.draw()
    for i in range(4):
        rect = Rect((WIDTH//2-i*WIDTH//8-WIDTH//16-5,0),(10,HEIGHT))
        screen.draw.filled_rect(rect,(128,128,128))
        rect = Rect((WIDTH//2+i*WIDTH//8+WIDTH//16-5,0),(10,HEIGHT))
        screen.draw.filled_rect(rect,(128,128,128))

    for p in p1:
        p.draw()

    for p in p2:
        p.draw()

    ball.draw()
    screen.draw.text(str(gate2.points)+":"+str(gate1.points),color="white",midtop=(WIDTH//2-2,30),fontsize=60)

def update():
    if keyboard.w:
        for p in p1:
            if p.active:
                p.up()

    if keyboard.s:
        for p in p1:
            if p.active:
                p.down()

    if keyboard.up:
        for p in p2:
            if p.active:
                p.up()

    if keyboard.down:
        for p in p2:
            if p.active:
                p.down()

    if keyboard.kp4 or keyboard.kp5 or keyboard.kp6 or keyboard.KP_PLUS:
        for p in p2:
            p.active = False
        if keyboard.KP_PLUS:
            p2[0].active = True
        if keyboard.kp6:
            p2[1].active = True
            p2[2].active = True               
            p2[3].active = True               
            p2[4].active = True               
        if keyboard.kp5:
            p2[5].active = True
            p2[6].active = True               
            p2[7].active = True               
        if keyboard.kp4:
            p2[8].active = True               
            p2[9].active = True               
            p2[10].active = True
            
    if keyboard.f or keyboard.g or keyboard.h or keyboard.j:
        for p in p1:
            p.active = False
        if keyboard.f:
            p1[0].active = True
        if keyboard.g:
            p1[1].active = True
            p1[2].active = True               
            p1[3].active = True               
            p1[4].active = True               
        if keyboard.h:
            p1[5].active = True
            p1[6].active = True               
            p1[7].active = True               
        if keyboard.j:
            p1[8].active = True               
            p1[9].active = True               
            p1[10].active = True      

    ball.update(p1,p2)    
    gate1.update(ball)
    gate2.update(ball)       

p1 = [
    Player(WIDTH//2-3*WIDTH//8-WIDTH//16,HEIGHT//2,(255,0,0),HEIGHT-R,R),
    Player(WIDTH//2-2*WIDTH//8-WIDTH//16,HEIGHT//5,(255,0,0),HEIGHT//5*2-R,HEIGHT//5*0+R),
    Player(WIDTH//2-2*WIDTH//8-WIDTH//16,HEIGHT//5*2,(255,0,0),HEIGHT//5*3-R,HEIGHT//5*1+R),
    Player(WIDTH//2-2*WIDTH//8-WIDTH//16,HEIGHT//5*3,(255,0,0),HEIGHT//5*4-R,HEIGHT//5*2+R),
    Player(WIDTH//2-2*WIDTH//8-WIDTH//16,HEIGHT//5*4,(255,0,0),HEIGHT//5*5-R,HEIGHT//5*3+R),
    Player(WIDTH//2-0*WIDTH//8-WIDTH//16,HEIGHT//4,(255,0,0),HEIGHT//4*2-R,HEIGHT//4*0+R),
    Player(WIDTH//2-0*WIDTH//8-WIDTH//16,HEIGHT//4*2,(255,0,0),HEIGHT//4*3-R,HEIGHT//4*1+R),
    Player(WIDTH//2-0*WIDTH//8-WIDTH//16,HEIGHT//4*3,(255,0,0),HEIGHT//4*4-R,HEIGHT//4*2+R),
    Player(WIDTH//2+1*WIDTH//8+WIDTH//16,HEIGHT//4,(255,0,0),HEIGHT//4*2-R,HEIGHT//4*0+R),
    Player(WIDTH//2+1*WIDTH//8+WIDTH//16,HEIGHT//4*2,(255,0,0),HEIGHT//4*3-R,HEIGHT//4*1+R),
    Player(WIDTH//2+1*WIDTH//8+WIDTH//16,HEIGHT//4*3,(255,0,0),HEIGHT//4*4-R,HEIGHT//4*2+R),
]
p1[5].active = True
p1[6].active = True
p1[7].active = True

p2 = [
    Player(WIDTH//2+3*WIDTH//8+WIDTH//16,HEIGHT//2,(0,0,255),HEIGHT-R,R),
    Player(WIDTH//2+2*WIDTH//8+WIDTH//16,HEIGHT//5,(0,0,255),HEIGHT//5*2-R,HEIGHT//5*0+R),
    Player(WIDTH//2+2*WIDTH//8+WIDTH//16,HEIGHT//5*2,(0,0,255),HEIGHT//5*3-R,HEIGHT//5*1+R),
    Player(WIDTH//2+2*WIDTH//8+WIDTH//16,HEIGHT//5*3,(0,0,255),HEIGHT//5*4-R,HEIGHT//5*2+R),
    Player(WIDTH//2+2*WIDTH//8+WIDTH//16,HEIGHT//5*4,(0,0,255),HEIGHT//5*5-R,HEIGHT//5*3+R),
    Player(WIDTH//2+0*WIDTH//8+WIDTH//16,HEIGHT//4,(0,0,255),HEIGHT//4*2-R,HEIGHT//4*0+R),
    Player(WIDTH//2+0*WIDTH//8+WIDTH//16,HEIGHT//4*2,(0,0,255),HEIGHT//4*3-R,HEIGHT//4*1+R),
    Player(WIDTH//2+0*WIDTH//8+WIDTH//16,HEIGHT//4*3,(0,0,255),HEIGHT//4*4-R,HEIGHT//4*2+R),
    Player(WIDTH//2-1*WIDTH//8-WIDTH//16,HEIGHT//4,(0,0,255),HEIGHT//4*2-R,HEIGHT//4*0+R),
    Player(WIDTH//2-1*WIDTH//8-WIDTH//16,HEIGHT//4*2,(0,0,255),HEIGHT//4*3-R,HEIGHT//4*1+R),
    Player(WIDTH//2-1*WIDTH//8-WIDTH//16,HEIGHT//4*3,(0,0,255),HEIGHT//4*4-R,HEIGHT//4*2+R)
]

p2[5].active = True
p2[6].active = True
p2[7].active = True

ball = Ball()
gate1 = Gate(40,HEIGHT//2-100)
gate2 = Gate(WIDTH-50,HEIGHT//2-100)