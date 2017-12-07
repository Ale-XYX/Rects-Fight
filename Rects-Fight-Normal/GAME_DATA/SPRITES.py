# SPRITES
import pygame
import GLOBAL as g
import MEDIA as m
import DICTIONARY as d

pygame.init()

# Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, enemy_bullets, direction, color, *groups):
        super().__init__(*groups)
        self.image = d.GAME_DICT[color.upper()]['PLAYER_IMAGE']
        self.color = d.GAME_DICT[color.upper()]['COLOR']
        self.bullet_image = d.GAME_DICT[color.upper()]['BULLET_IMAGE']
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
        self.rect.clamp_ip(g.PLAY_AREA)
        collided = pygame.sprite.spritecollide(self, self.enemy_bullets, True)
        for bullet in collided:
            self.health -= 1
            m.MEDIA['hit_sound'].play()
            if self.health <= 0:
                m.MEDIA['die_sound'].play()
                self.kill()
                self.toggle = True

# Bullet
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
            if not g.PLAY_AREA.contains(self):
                self.kill()
                
# Selector
class Selector(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = m.MEDIA['selector']
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(pos)
    def update(self):
        self.rect.center = self.pos
        if self.pos[0] > 470:
            self.pos[0] = 30
        elif self.pos[0] < 0:
            self.pos[0] = 470

# Larger Selector
class SelectorBig(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = m.MEDIA['selectorbig']
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(pos)
    def update(self):
        self.rect.center = self.pos
        if self.pos[1] > 350:
            self.pos[1] = 250
        elif self.pos[1] <= 150:
            self.pos[1] = 350
    
