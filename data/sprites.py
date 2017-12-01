import pygame
import gamewide
import media32 as m32

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, enemy_bullets, image, direction, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)
        self.fire_direction = pygame.math.Vector2(direction)
        self.health = 3
        self.enemy_bullets = enemy_bullets
        self.toggle = False
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        self.rect.clamp_ip(gamewide.playarea)
        collided = pygame.sprite.spritecollide(self, self.enemy_bullets, True)
        for bullet in collided:
            self.health -= 1
            m32.MEDIA[27].play()
            if self.health <= 0:
                m32.MEDIA[25].play()
                self.kill()
                self.toggle = True
                
                
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not gamewide.playarea.contains(self):
                self.kill()
                
