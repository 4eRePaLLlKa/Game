
from pygame import *
from button import Button
from sprite import Player, GameSprite, Wall


window = display.set_mode((700,500))

background_image = image.load("arena.png")
background = transform.scale(background_image, (700,500))



game = True
clock = time.Clock()
run = False

btn1 = Button('start.png',275,100,150,50)
btn2 = Button('exit.png',275,200,150,50)

player = Player('Survivor.png',25,200,75,75,3)

wall1 = Wall(200,35, 110,75, transperancy=0)
wall2 = Wall(200,35, 110,175, transperancy=0)
wall3 = Wall(200,35, 110,275, transperancy=0)
wall4 = Wall(200,35, 110,375, transperancy=0)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False

    

    if run:
        window.blit(background, (0,0))
        player.draw(window)
        player.move()


        wall1.draw(window)
        wall2.draw(window)
        wall3.draw(window)
        wall4.draw(window)
        
    else:
        window.fill((0,0,0))
        if btn1.draw(window):
            run = True
            print("Press")
        if btn2.draw(window):
            game = False        
    

    display.update()
    clock.tick(60)


