

HEIGHT=800
WIDTH=1000
X1=100
Y1=100
X2=WIDTH-100
Y2=HEIGHT-100
SPEED = 3
TITLE="Tron"

class Game(Actor):
    start = True


class Player(Actor):
    xv,vy = 0,0
    alive = False 
    points = 0
    turbo = 50

    def update(self):
        c = screen.surface.get_at((int(self.center[0]+self.vx*2), int(self.center[1]+self.vy*2)))
        #print(c)
        if c == (40,50,50,255) or c== (150, 150, 150,255) or c == (0,0,0,255):
            self.draw()
            self.center= (self.center[0]+self.vx, self.center[1]+self.vy)
            self.alive = True
        else:
            #print("hej")
            self.alive = False 

def update():
    if keyboard.a and p1.vx == 0:
        p1.vx=-SPEED
        p1.vy = 0
    if keyboard.d and p1.vx == 0:
        p1.vx = SPEED
        p1.vy = 0
    if keyboard.w and p1.vy == 0:
        p1.vx = 0
        p1.vy = -SPEED
    if keyboard.s and p1.vy == 0:
        p1.vx = 0
        p1.vy = SPEED

    if keyboard.left and p2.vx == 0:
        p2.vx=-SPEED
        p2.vy = 0
    if keyboard.right and p2.vx == 0:
        p2.vx = SPEED
        p2.vy = 0
    if keyboard.up and p2.vy == 0:
        p2.vx = 0
        p2.vy = -SPEED
    if keyboard.down and p2.vy == 0:
        p2.vx = 0
        p2.vy = SPEED


    if not p1.alive:
        p1.image="p1dead.png"
        p1.draw()
    elif p1.alive and p2.alive:
        p1.update()
        if keyboard.t and p1.turbo>0:
            p1.update()
            p1.turbo = p1.turbo - 1

    if not p2.alive:
        p2.image="p2dead.png"
        p2.draw()
    elif p1.alive and p2.alive:
        p2.update()
        if keyboard.kp3 and p2.turbo>0:
            p2.update()
            p2.turbo = p2.turbo - 1

    if not p1.alive or not p2.alive:
        if keyboard.space:
            if p1.alive:
                p1.points = p1.points + 1
            elif p2.alive:
                p2.points = p2.points + 1
            screen.fill((0,0,0))
            game.start = True
            p1.center = (WIDTH//4,HEIGHT//2)
            p1.vx = SPEED
            p1.vy = 0
            p1.image = "p1.jpg"
            p1.alive = True
            p2.center = (WIDTH//4*3,HEIGHT//2)
            p2.vx = -SPEED
            p2.vy = 0
            p2.image = "p2.jpg"
            p2.alive = True
            p1.turbo = 50
            p2.turbo = 50

def draw():
    if game.start:
        rect = Rect((X1-15,Y1-15),(X2-70,Y2-70))
        screen.draw.filled_rect(rect,(5,5,5))
        rect = Rect((X1,Y1),(X2-100,Y2-100))
        screen.draw.filled_rect(rect,(40,50,50))

        for i in range(X1+25,X2,25):
            screen.draw.line((i,Y1), (i,Y2), (150, 150, 150))
        for j in range(Y1+25,Y2,25):
            screen.draw.line((X1,j), (X2,j), (150, 150, 150))

        screen.draw.text(str(int(p1.points)),color=(51,204,153),midtop=(WIDTH//2-50,HEIGHT//10*9),fontsize=60)
        screen.draw.text(str(int(p2.points)),color=(255,102,255),midtop=(WIDTH//2+50,HEIGHT//10*9),fontsize=60)
        screen.draw.text(":",color="white",midtop=(WIDTH//2,HEIGHT//10*9),fontsize=60)

        game.start = False
    elif not p1.alive or not p2.alive:
        screen.draw.text("Press [spacebar] to start",color="white",midtop=(WIDTH//2,HEIGHT//4*3),fontsize=60)
    

    rect = Rect((0,0),(X1-25,HEIGHT))
    screen.draw.filled_rect(rect,(0,0,0))
    for i in range(p1.turbo):
        rect = Rect((WIDTH//15-25,Y2 - i*10),(15,9))
        screen.draw.filled_rect(rect,(51,204,153))

    rect = Rect((X2+25,0),(WIDTH,HEIGHT))
    screen.draw.filled_rect(rect,(0,0,0))
    for i in range(p2.turbo):
        rect = Rect((WIDTH//15*14+25,Y2 - i*10),(15,9))
        screen.draw.filled_rect(rect,(255,102,255))
    screen.draw.text("Turbo",color=(51,204,153),midtop=(WIDTH//15-15,Y2+10),fontsize=30)
    screen.draw.text("[t]",color=(51,204,153),midtop=(WIDTH//15-15,Y2+30),fontsize=30)
    screen.draw.text("Turbo",color=(255,102,255),midtop=(WIDTH//15*14+25,Y2+10),fontsize=30)
    screen.draw.text("[3]",color=(255,102,255),midtop=(WIDTH//15*14+25,Y2+30),fontsize=30)
    screen.blit("key1.png",(WIDTH//15+100,Y2+15))
    screen.blit("key2.png",(WIDTH//15*14-180,Y2+15))

# wstepne rysowanie planszy
game = Game("pix.jpg")

p1=Player("p1.jpg",center=(WIDTH//4,HEIGHT//2))
p1.vx = SPEED
#p1.color = (51,204,153)
p2=Player("p2.jpg",center=(WIDTH//4*3,HEIGHT//2))
p2.vx = -SPEED
#p2.color = (255,102,255)
