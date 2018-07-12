# first install pgzero: pip install pgzero
# to run game: pgzrun flappybird.py

import random
HEIGHT=708
WIDTH=400
TITLE="Flappy Bird"


bird=Actor("bird1.png",(75,200))
bird.dead=False
bird.score=-1
bird.vy=0

top=Actor("top.png",anchor=("left","bottom"),pos=(-100,0))
bottom=Actor("bottom.png",anchor=("left","top"),pos=(-100,0))


def draw():
    screen.clear()
    screen.blit("background.png",(0,0))
    top.draw()
    bottom.draw()
    bird.draw()
    screen.draw.text(str(bird.score),color="white",midtop=(WIDTH//2,10),fontsize=70,shadow=(1,1))
#alien.topright=0,0


def update_pipes():
    top.left=top.left-3
    bottom.left=bottom.left-3
    if top.right<0:
        bird.score=bird.score+1
        gap=random.randint(200,HEIGHT-200)
        top.pos = (WIDTH,gap-130//2)
        bottom.pos = (WIDTH,gap+130//2)




def update(dt):
    update_pipes()
    uy=bird.vy
    bird.vy=bird.vy+2000.0*dt
    bird.y=bird.y+(uy+bird.vy)*0.5*dt

    bird.x=75

    if not bird.dead:
        if bird.vy<-3:
            bird.image="bird2.png"
        else:
            bird.image="bird1.png"

    if bird.colliderect(top) or bird.colliderect(bottom):
        bird.dead=True
        bird.image="birddead.png"
    if not 0<bird.y<720:
        bird.y=200
        bird.dead=False
        bird.score=0
        bird.vy=0
        gap=random.randint(200,HEIGHT-200)
        top.pos = (WIDTH,gap-130//2)
        bottom.pos = (WIDTH,gap+130//2)
    
def on_key_down(key):
    if key==keys.SPACE and not bird.dead:
        bird.vy=-500
    

