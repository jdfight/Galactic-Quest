import random
import pygame
import dirtytext
import utils
import ship
import shooter
import simple_button

from pygame.locals import *

class SplashGS():

    def __init__(self, screen):

        self.screen = screen
        self.allsprites =  pygame.sprite.LayeredDirty()
        
        self.background = pygame.Surface(self.screen.get_size())
        self.background, self.rect =  utils.load_image('nasa_flame.jpg', -1)
        self.player_ship = ship.ObjShip()
        
        button_image, button_rect = utils.load_image('buttons_red.png', -1)
        button_frames  = [ (0,0,116,31), (116,0,116,31), (233,0,116,31) ]
        self.button = simple_button.BtnSimple(button_image, button_rect, button_frames)
        self.button.rect.topleft = 270, 240
    
        pygame.font.init()
        self.default_font = pygame.font.SysFont("Arial", 48)
        self.screen.blit(self.background, (0,0))

        self.button_label = dirtytext.DirtyText ("Play Again", "None", 286, 245, 24, (255, 255, 255))
        self.message_victory = dirtytext.DirtyText( "You Won!", "None", 275, 200, 32, (255, 255, 0))
        
        self.allsprites.add(self.message_victory) 
        self.allsprites.add(self.button)
        self.allsprites.add(self.button_label)
        self.allsprites.add(self.player_ship)

        self.allsprites.clear(self.screen, self.background)
        
        pygame.display.flip()
        self.running = True
        self.alive = True

    def foo(self):
        print "foo"
        #self.die()
        pygame.display.flip()
        shooter.switch_state(self, "game")

    def die(self):
        self.alive = False
        del self.allsprites
        del self.screen
        del self.background
        del self.button
        del self.message_victory
        del self

    def update(self):
        if self.alive:            
            self.allsprites.update()
            rects = self.allsprites.draw(self.screen)
            pygame.display.update(rects)
            if self.button.check_state():
                self.foo()

