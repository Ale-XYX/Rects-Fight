import pygame
import datetime
import var as v
import media as m
logat = str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'SPRITES: '

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, enemy_bullets, direction, color, *groups):
        super().__init__(*groups)
        self.image = m.PLAYER_MEDIA[color]['player_image']
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)
        self.fire_direction = pygame.math.Vector2(direction)
        self.health = 3
        self.enemy_bullets = enemy_bullets
        self.toggle = False
        self.color = m.PLAYER_MEDIA[color]['color']
        self.bullet_image = m.PLAYER_MEDIA[color]['bullet_image']
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        self.rect.clamp_ip(v.playarea)
        collided = pygame.sprite.spritecollide(self, self.enemy_bullets, True)
        for bullet in collided:
            self.health -= 1
            m.MEDIA['hit'].play()
            if self.health <= 0:
                m.MEDIA['die'].play()
                self.kill()
                self.toggle = True
                
print(logat + 'Loaded Player Sprite')

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
            if not v.playarea.contains(self):
                self.kill()
                
print(logat + 'Loaded Bullet Sprite')

class Selector(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = m.MEDIA['selector']
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(pos)
    def update(self):
        self.rect.center = self.pos
        if self.pos[0] == 470:
            self.pos[0] = 85
        if self.pos[0] == 30:
            self.pos[0] = 415

print(logat + 'Loaded Selector Sprite')
                
