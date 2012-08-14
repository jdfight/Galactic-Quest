import pygame
import utils
import random

from pygame.locals import *

class ObjShot(pygame.sprite.DirtySprite):
    """Simple basic shot"""
    def __init__ (self, id_num,  sx, sy):
        pygame.sprite.DirtySprite.__init__(self)
        self.id_num = id_num
        if id_num == 1:   
            self.limit = -23
            self.speed = -4
            self.image, self.rect = utils.load_image('shot1.png', -1)
        else:
            self.limit = 503
            self.speed = 8
            self.image, self.rect = utils.load_image('shot1_d.png', -1)
      
       # screen = pygame.display.get_surface()
       # self.area = screen.get.rect()
        self.rect.topleft = sx, sy
        self.dirty = 1

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if self.id_num == 1 and self.rect.topleft[1] < self.limit or self.id_num == 2 and self.rect.topleft[1] > self.limit:
            self.dirty = 0
            self.die()
        else:
            self.dirty = 1

    def die(self):
        pygame.sprite.Sprite.kill(self)
        self.kill()

        
