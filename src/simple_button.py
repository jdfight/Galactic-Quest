import pygame
import utils
import random
import spritesheet

from pygame.locals import *

class BtnSimple(pygame.sprite.DirtySprite, spritesheet.Spritesheet):
    """Simple Button with Init, Rollover and Pressed states """
    def __init__ (self, sheet, rect, frames):
        pygame.sprite.DirtySprite.__init__(self)
        spritesheet.Spritesheet.__init__(self, sheet)
       
        self.rect = rect
        self.frames = frames
        self.frame_index = 0

        self.images = self.imgsat(self.frames, -1)
        self.image = self.images[0]
        self.dirty = 1
        self.state = False

    def checkmouse(self):
        mouse_pos = pygame.mouse.get_pos()
        # print self.rect.topleft[0]
        if  mouse_pos[0] >= self.rect.topleft[0] and mouse_pos[0] <= self.rect.topleft[0] + 116 and mouse_pos[1] >= self.rect.topleft[1] and mouse_pos[1] <= self.rect.topleft[1] + 31:
            return True
        else:
            return False
        
    def check_state(self):
        return self.state
    
    def update(self):
        if self.checkmouse():
            if pygame.mouse.get_pressed()[0]:
                self.frame_index = 2
                self.state = True
            else:
                self.frame_index = 1
                self.state = False
            
        else:
            self.frame_index = 0
            self.state = False
      
        self.image = self.images[self.frame_index]
    
        self.dirty = 1

    def die(self):
        del self.images
        del self.sheet
        #del frames
        pygame.sprite.Sprite.kill(self)
        self.kill()

        
