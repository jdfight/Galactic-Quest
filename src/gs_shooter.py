import random
import pygame
import star
import ship
import shot
import enemyship
import explosion
import dirtytext
import shooter
 
from pygame.locals import *

class ShooterGS():

    def __init__(self, screen):
        self.e_group = pygame.sprite.Group()
        self.p_group = pygame.sprite.Group()
        self.allsprites =  pygame.sprite.LayeredDirty()
        self.p_bullets = pygame.sprite.Group()
        self.e_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.stars = []

        random.seed()
      
        self.screen = screen
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        pygame.font.init()
        self.default_font = pygame.font.SysFont("Arial", 48)
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()
        self.Ship = ship.ObjShip()
        self.Enemy = enemyship.ObjShip()
        self.player_dead = False
        self.e_spawn = True
        self.wave_count = 0
        self.message_victory = dirtytext.DirtyText( "You Won!", "None", 266, 200, 32, (255, 255, 0))

        for i in range (0, 80):
            self.allsprites.add( star.ObjStar(random.randrange(1,4)))

        self.allsprites.add(self.Enemy)   
        self.e_group.add(self.Enemy)

        self.allsprites.add(self.Ship)
        self.p_group.add(self.Ship)
        
        self.allsprites.clear(self.screen, self.background)
        self.ecount = 1

        self.running = True
        self.clock = pygame.time.Clock()
        self.ctime = pygame.time.get_ticks()
        self.ltime = self.ctime
        self.alive = True
        self.shooting = False
        
    def spawn_enemy(self):
        spawn = enemyship.ObjShip()
        self.e_group.add(spawn)
        spawn.shot_assign(self.enemy_shot)
        self.allsprites.add(spawn)

    def enemy_shot(self, ex, ey):
        e_shot = shot.ObjShot(2, ex, ey)
        self.e_bullets.add(e_shot)
        self.allsprites.add(e_shot)

    def spawn_player(self):
        Ship = ship.ObjShip()
        self.p_group.add(Ship)
        self.allsprites.add(Ship)
        return Ship

    def die(self):
        self.alive = False
        del self.allsprites
        del self.p_group
        del self.e_group
        del self.e_bullets
        del self.enemies
        del self.stars
        del self.screen
        del self.background
        del self.message_victory
        del self
        
    def update(self):
        if self.alive:
            self.ctime = pygame.time.get_ticks()
            if self.ctime - self.ltime > 1000:
                if self.player_dead:
                    self.Ship =  self.spawn_player()
                    self.player_dead = False
                elif self.e_spawn == True and self.ecount < 30:     
                    self.spawn_enemy()
                    self.ecount += 1
                elif self.ecount == 30:
                    self.e_spawn = False
                self.ltime = self.ctime

            key = pygame.key.get_pressed()
            if  key[pygame. K_SPACE] and not self.shooting and self.player_dead == False:
                self.bullet = shot.ObjShot(1, self.Ship.rect.topleft[0]+14, self.Ship.rect.topleft[1])
                self.allsprites.add(self.bullet)
                self.p_bullets.add(self.bullet)
                self.shooting = True
            elif not key[pygame.K_SPACE]:
                self.shooting = False
                
            self.allsprites.update()
            self.p_bullets.update()

                # Draw Everything
            rects = self.allsprites.draw(self.screen)
            pygame.display.update(rects)

            collide1 = pygame.sprite.groupcollide(self.e_group, self.p_bullets, True, True)
            collide2 = pygame.sprite.groupcollide(self.p_group, self.e_bullets, True, True)

            if collide1 != {} and self.alive:
                for sprite in collide1:
                    explode = explosion.ObjExplode()
                    explode.rect.topleft = sprite.rect.topleft
                    self.allsprites.add(explode)
                    self.wave_count += 1
                    if self.wave_count == 30:
                        self.ecount = 0
                        self.allsprites.add(self.message_victory)
                        self.allsprites.update()
                        rects = self.allsprites.draw(self.screen)
                        pygame.display.update(rects)
                        pygame.display.flip()
                        shooter.switch_state(self, "test")
                      

            if collide2 != {} and self.alive :
                for sprite in collide2:
                    explode = explosion.ObjExplode()
                    explode.rect.topleft = sprite.rect.topleft
                    sprite.die()
                    self.allsprites.add(explode)
                    self.player_dead = True
       

