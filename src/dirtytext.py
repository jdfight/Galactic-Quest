import pygame
import utils 
import random
import pygame.mouse

from pygame.locals import *

class DirtyText(pygame.sprite.DirtySprite):
    """Text rendered to a DirtySprite"""
    def __init__(self, text, font, sx, sy, size, color):
        pygame.sprite.DirtySprite.__init__(self)
        #pygame.font.init()
        self.font = pygame.font.SysFont(font, size)
        self.image = self.font.render(text, 1, color)
        self.rect = (sx, sy, 1, 1)
        self.dirty = 1
       

    def update(self):
       # Update
        self.dirty = 1

    def die(self):
        pygame.sprite.Sprite.kill(self)
        self.kill()
