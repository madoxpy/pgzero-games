HEIGHT=850
WIDTH=850
TITLE="Bomberman"

class Block(Actor):
    pass
class Brick(Actor):
    pass
class Player(Actor):
    health = 100

def newgame():
    for i in range(17):
        objs.append(Block("block.png",(i*52+5,10)))
        objs.append(Block("block.png",(i*52+5,HEIGHT-10)))
    for i in range(15):
        objs.append(Block("block.png",(5,i*52+60)))
        objs.append(Block("block.png",(WIDTH-12,i*52+60)))

    file = open("map1.dat")
    i = 1
    for line in file:
        for j in range(len(line)):
            if line[j] == "#":
                objs.append(Block("brick.png",(i*52+5,j*52+55)))
        i = i + 1


def draw():
    screen.fill((148, 146, 255))
    for obj in objs:
        obj.draw()
    player1.draw()
    player2.draw()

def update():
    player1.clock = (player1.clock + 1)%60

    if keyboard.w:
        player1.y = player1.y - 1
        for obj in objs:
            if player1.colliderect(obj):
                player1.y = player1.y + 1
        player1.image = str(int(player1.clock/20)+1) + "player1up.png"
    elif keyboard.s:
        player1.y = player1.y + 1
        for obj in objs:
            if player1.colliderect(obj):
                player1.y = player1.y - 1
        player1.image = str(int(player1.clock/20)+1) + "player1down.png"
    elif keyboard.a:
        player1.x = player1.x - 1
        for obj in objs:
            if player1.colliderect(obj):
                player1.x = player1.x + 1
        player1.image = str(int(player1.clock/20)+1) + "player1left.png"
    elif keyboard.d:
        player1.x = player1.x + 1
        for obj in objs:
            if player1.colliderect(obj):
                player1.x = player1.x - 1
        player1.image = str(int(player1.clock/20)+1) + "player1right.png"

    if keyboard.up:
        player2.y = player2.y - 1
        for obj in objs:
            if player2.colliderect(obj):
                player2.y = player2.y + 1
    if keyboard.down:
        player2.y = player2.y + 1
        for obj in objs:
            if player2.colliderect(obj):
                player2.y = player2.y - 1
    if keyboard.left:
        player2.x = player2.x - 1
        for obj in objs:
            if player2.colliderect(obj):
                player2.x = player2.x + 1
    if keyboard.right:
        player2.x = player2.x + 1
        for obj in objs:
            if player2.colliderect(obj):
                player2.x = player2.x - 1


objs = []
newgame()
player1 = Player("2player1down.png",(55,55))
player2 = Player("2player2down.png",(WIDTH-55,HEIGHT-55))
player1.clock = 0
