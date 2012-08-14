import pygame
import utils
import random
import spritesheet

from pygame.locals import *

class ObjExplode(pygame.sprite.DirtySprite, spritesheet.Spritesheet):
    """Explosion spritesheet"""
    def __init__ (self):
        pygame.sprite.DirtySprite.__init__(self)
        sheet, self.rect =utils.load_image('explode1.png', -1)
        spritesheet.Spritesheet.__init__(self, sheet)
        
        self.ctime = pygame.time.get_ticks()
        self.ltime = self.ctime
        self.speed = -12
        self.delaycount = 0
    
        self.frames = [(1,1,32,32), (33,1,32,32), (65,1,32,32), (99,1,32,32), (132,1,32,32), (165, 1, 32,32)]
        self.frame_index = 1
        self.images = self.imgsat(self.frames, -1)
        self.image = self.images[0]
    
        self.rect.topleft = 100, 100
        self.dirty = 1

    def update(self):
        self.ctime = pygame.time.get_ticks()
        if self.ctime - self.ltime  > 50:
           self.image = self.images[self.frame_index]
           self.frame_index += 1
           self.ltime = self.ctime
           if self.frame_index > 5:
               self.die()
           self.delaycount = 0
        else:
           self.delaycount += 1
        self.dirty = 1

    def die(self):
        del self.images
        pygame.sprite.Sprite.kill(self)
        self.kill()

        
