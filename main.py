
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

#music
mixer.init()
mixer.music.load("zombie_sound.mp3")
mixer.music.play()
ak = mixer.Sound("ak47_sound.ogg")


game = True
clock = time.Clock()
run = False

btn1 = Button('start.png',275,100,150,50)
btn2 = Button('exit.png',275,200,150,50)

player = Player('Survivor.png',25,350,55,55,5)

wall1 = Wall(200,35, 110,75, transperancy=0)
wall2 = Wall(200,35, 110,175, transperancy=0)
wall3 = Wall(200,35, 110,275, transperancy=0)
wall4 = Wall(200,35, 110,375, transperancy=0)



score = 0 

max_score = 30


lose = font1.render("You Lose", True, (255,0,0))
win = font1.render("You Win", True, (255,255,255))

wall = sprite.Group()
wall.add(wall1)
wall.add(wall2)
wall.add(wall3)
wall.add(wall4)

finish = False
enemys = sprite.Group()
bullets = sprite.Group()

points = [15,120,220,320,420]
img_enemy = ["zombie1.png","zombie2.png","zombie3.png"]


for i in range(6):
    enemy1 = Enemy(img_enemy[randint(0,2)],randint(640,650),points[randint(0,4)],30,45,randint(1,2))

    enemys.add(enemy1)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
            if e.key == K_SPACE:
                ak.play()
                bullets.add(player.fire())

    

    if run:
        window.blit(background, (0,0))
        player.draw(window)
        player.move()


        img = font1.render("Score: "+str(score), True,(255,255,255))
        window.blit(img, (20,450))




        wall1.draw(window)
        wall2.draw(window)
        wall3.draw(window)
        wall4.draw(window)
        

        for b in bullets:
            b.update(window)

        for e in enemys:
            e.update(window)

        collides = sprite.groupcollide(enemys, bullets,True,True)
        for c in collides:
            score = score + 1
            enemy1 = Enemy(img_enemy[randint(0,2)],randint(640,650),points[randint(0,4)],30,45,randint(1,2))
            enemys.add(enemy1)


        collides = sprite.groupcollide(wall, bullets,False,True)
     

    else:
        window.fill((0,0,0))
        
        if btn1.draw(window):
            run = True
            
        if btn2.draw(window):
            game = False        
    

    display.update()
    clock.tick(60)


