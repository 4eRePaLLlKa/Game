from pygame import *

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
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= 5
        elif keys[K_DOWN]:
            self.rect.y += 5

    def fire(self):
        pass


class Enemy(GameSprite):
    def move(self):
        pass

class Wall(GameSprite):
    def __init__(self,width,height,x,y,color,transperancy=255):
        self.wall = Surface((50,50))
        self.wall.set_alpha(transperancy)
        self.wall.fill(0,0,0)
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def