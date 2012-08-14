import pygame
import utils 
import random
import pygame.mouse

from pygame.locals import *

class ObjShip(pygame.sprite.DirtySprite):
    """Basic Ship Type"""
    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.targetPos = [280, 340]
        self.image, self.rect = utils.load_image('ShipG.png', -1)
        self.speed = 4

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 280, 340
        self.dirty = 1
       

    def update(self):
       # Update
        key = pygame.key.get_pressed()
        incX = 0
        incY = 0
        self.dirty = 1
        
        if  key[pygame. K_LEFT]:
            incX = -self.speed
        elif key[pygame.K_RIGHT]:
            incX = self.speed
        if  key[pygame. K_UP]:
            incY = -self.speed
        elif key[pygame.K_DOWN]:
            incY = self.speed
        if  incX != 0 or incY != 0:
            if self.rect.topleft[0] + incX < 0 or self.rect.topleft[0] + incX > 640 - self.rect.width:
                incX = 0
            if self.rect.topleft[1] + incY < 0 or  self.rect.topleft[1] + incY > 480 - self.rect.height:
                incY = 0

            self.rect =  self.rect.move(incX, incY)
           # self.dirty = 1

    def die(self):
        self.shot_call = None
        pygame.sprite.Sprite.kill(self)
        self.kill()
