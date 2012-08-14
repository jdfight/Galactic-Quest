import random
import pygame
import star
import ship
import shot
import enemyship
import explosion
import dirtytext
import state
import gs_shooter
import gs_testsplash1

from pygame.locals import *

SCREEN_W = 640
SCREEN_H = 480
YELLOW = (255, 255, 0)

pygame.init()
pygame.display.set_caption('Shooter')
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H),  pygame.DOUBLEBUF)

state_manager = state.GameState()

def switch_state(gstate, switchto):
    global state_manager
    gstate.die()
    if switchto == "test":
        new_gs = gs_testsplash1.SplashGS(screen)
    elif switchto == "game":
        new_gs = gs_shooter.ShooterGS(screen)
 
    state_manager.remove_state(gstate)
    if new_gs:
        state_manager.add_state(new_gs)

def main():
    pygame.init()
    pygame.display.set_caption('Shooter')
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H),  pygame.DOUBLEBUF)
    gs = gs_shooter.ShooterGS(screen)
   
    state_manager.add_state(gs)
    
    running = True
    clock = pygame.time.Clock()
    ctime = pygame.time.get_ticks()
    ltime = ctime
   
    while running:
        clock.tick(60)
        ctime = pygame.time.get_ticks()
        state_manager.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
              
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False      

      
           
if __name__ == '__main__':
    main()
