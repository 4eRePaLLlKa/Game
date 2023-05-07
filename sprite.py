from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,image_name,x,y,width,height,speed):
        self.image = transform.scale(image.load(image_name),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    self.img_1 = transform.scale(image.load("bullet.png"), (10,15))
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP] == True and self.rect.y != 20:
            self.rect.y = self.rect.y - self.speed 
        elif keys[K_DOWN] == True and self.rect.y != 410:
            self.rect.y = self.rect.y + self.speed 

def fire(self):
        if self.image == self.img_1:
            bullet = Bullet(self.rect.centerx, self.rect.centery)
        return bullet


class Bullet(sprite.Sprite):
    def __init__(self, x,y):
        self.bull = Surface((20,20))
        self.bull.fill((255,0,0))
        self.rect = self.bull.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self, window):
        window.blit(self.bull, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def update(self,window):
        self.rect.x = self.rect.x - self.speed
        points = [15,120,220,320,420]
        global lost
        if self.rect.x < 200:
            self.rect.x = randint(640,650)        
            self.rect.y = points[randint(0,4)]
            self.speed = randint(1,2)
        window.blit(self.image,(self.rect.x,self.rect.y))




class Wall():
    def __init__(self, width,height, x,y, color=(255,255,255), transperancy=255):
        self.wall = Surface((width,height))
        self.wall.set_alpha(transperancy)
        self.wall.fill(color)
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.wall, (self.rect.x, self.rect.y))