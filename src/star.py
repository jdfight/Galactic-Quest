import pygame
import utils 
import random

class ObjStar(pygame.sprite.DirtySprite):
    """Basic Star Type"""
    def __init__(self, level):
        pygame.sprite.DirtySprite.__init__(self)
        self.level = level
        self.speed = level * 2
       
        if level == 1:
            self.image, self.rect = utils.load_image('star_s.png', -1)
        elif level == 2:
            self.image, self.rect = utils.load_image('star_m.png', -1)
        else:
            self.image, self.rect = utils.load_image('star_l.png', -1)
            self.speed = 6
       
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = random.randrange(0,640), random.randrange(0, 480)
        self.dirty = 1
       

    def update(self):
       
        self.rect = self.rect.move(0, self.speed)
        if self.rect.topleft[1] > 490:
            self.rect.topleft = random.randrange(4 ,640), random.randrange(-480, -4) 
            self.dirty = 0
       
        elif self.rect.topleft[1] < 500 and self.rect.topleft[1] > -4:
         
            self.dirty = 1
        else:
            self.dirty = 0     
 
