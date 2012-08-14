import os
import pygame

from pygame.locals import *
class Spritesheet:
    def __init__(self, sheet):
       self.sheet = sheet
    
    def imgat(self, rect, colorkey = None):
        rect = Rect(rect)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
                image.set_colorkey(colorkey, RLEACCEL)
        return image

    def imgsat(self, rects, colorkey = None):
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs
