import pygame
import utils
import random

from pygame.locals import *

random.seed()

class ObjShip(pygame.sprite.DirtySprite):
    """Simple basic shot"""
    def __init__ (self):
        pygame.sprite.DirtySprite.__init__(self)
        self.ctime = pygame.time.get_ticks()
        self.ltime = self.ctime
        self.speed = 2
        if random.randrange(0, 100) > 50:
            self.speed = -2
        self.speed_y = 3
        self.shot_call = None
        self.image, self.rect = utils.load_image('ShipE.png', -1)
       # screen = pygame.display.get_surface()
       # self.area = screen.get.rect()
        self.rect.topleft = random.randrange(10, 400), 0
        self.dirty = 1

    def update(self):
        self.ctime = pygame.time.get_ticks()
        if self.rect.topleft[1] < 120 and self.ctime - self.ltime > 2000 and self.shot_call:
            self.shot_call(self.rect.topleft[0] + self.rect.width/2, self.rect.topleft[1] + self.rect.height/2)
            self.ltime = self.ctime
        if self.rect.topleft[1] + self.speed_y < 0 or self.rect.topleft[1] + self.speed_y > 240:
            self.speed_y *= -1
        if self.rect.topleft[1] < 60:
            self.rect = self.rect.move(0, self.speed_y)
           # self.speed = 
            self.dirty = 1
#            self.die()
        elif self.rect.topleft[0] + self.speed < 0 or self.rect.topleft[0] + self.speed > 620:
            self.speed *= -1
            self.dirty = 1
            self.rect = self.rect.move(self.speed, self.speed_y)
        else:
            self.rect = self.rect.move(self.speed, self.speed_y)
            self.dirty = 1

    def die(self):
        self.shot_call = None
        pygame.sprite.Sprite.kill(self)
        self.kill()
        
    def shot_assign(self, f):
        self.shot_call = f
