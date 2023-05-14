
from pygame import *
from button import Button
from sprite import Player, GameSprite, Wall, Bullet, Enemy
from random import randint


window = display.set_mode((700,500))

background_image = image.load("arena.png")
background = transform.scale(background_image, (700,500))

font.init()
font1 = font.SysFont("Arial", 20)
img = font1.render("Score: ",True,(255,255,255))

game = True
clock = time.Clock()
run = False

btn1 = Button('start.png',275,100,150,50)
btn2 = Button('exit.png',275,200,150,50)

player = Player('Survivor.png',25,350,75,75,5)

wall1 = Wall(200,35, 110,75, transperancy=0)
wall2 = Wall(200,35, 110,175, transperancy=0)
wall3 = Wall(200,35, 110,275, transperancy=0)
wall4 = Wall(200,35, 110,375, transperancy=0)



bullets = sprite.Group()
bullets = []
enemys = []

for i in range(2):
    enemy1 = Enemy("zombie1.png",randint(640,650),20,30,45,randint(1,2))
    enemy2 = Enemy("zombie2.png",randint(640,650),320,30,45,randint(1,2))
    enemy3 = Enemy("zombie3.png",randint(640,650),420,30,45,randint(1,2))
    enemys.append(enemy1)
    enemys.append(enemy2)
    enemys.append(enemy3)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
            if e.key == K_SPACE:
                bullets.append(player.fire())

    

    if run:
        window.blit(background, (0,0))
        player.draw(window)
        player.move()

        window.blit(img, (20,450))
        wall1.draw(window)
        wall2.draw(window)
        wall3.draw(window)
        wall4.draw(window)
        

        for b in bullets:
            b.update(window)

        for e in enemys:
            e.update(window)



    else:
        window.fill((0,0,0))
        
        if btn1.draw(window):
            run = True
            print("Press")
        if btn2.draw(window):
            game = False        
    

    display.update()
    clock.tick(60)


