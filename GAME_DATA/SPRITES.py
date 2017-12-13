# SPRITES
import pygame
import GLOBAL as G
import DICTIONARY as D
import FUNCTION as F

pygame.init()

FUNC_DICT = {
    'BLUE': F.BIG_BULLET,
    'ORANGE': F.BIG_BULLET,
    'GREEN': F.SPLIT_BULLET,
    'YELLOW': F.SPLIT_BULLET,
    'RED': F.LASER_BEAM,
    'PURPLE': F.LASER_BEAM,
    'GREY': F.REVERSE_BULLET,
    'WHITE': F.REVERSE_BULLET,
    'RAINBOW': F.MULTI_BULLET
    }

# Player Sprite
class RECT(pygame.sprite.Sprite):
    def __init__(self, pos, enemy_bullets, direction, color, *groups):
        super().__init__(*groups)
        self.image = D.PLAYER_DICT[color.upper()]['PLAYER_IMAGE']
        self.color = D.PLAYER_DICT[color.upper()]['COLOR']
        self.bullet_image = D.PLAYER_DICT[color.upper()]['BULLET_IMAGE']
        self.params = D.PLAYER_DICT[color.upper()]['PARAMS']
        self.ability = FUNC_DICT[color.upper()]
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)
        self.fire_direction = (direction)
        self.health = 3
        self.enemy_bullets = enemy_bullets
        self.toggle = False
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        self.rect.clamp_ip(G.PLAY_AREA)
        collided = pygame.sprite.spritecollide(self, self.enemy_bullets, True)
        # Detects when a bullet is collided and then works out corresponding actions
        for bullet in collided:
            if bullet.type == 'BULLET':
                self.health -= 1
                D.MEDIA['hit_sound'].play()
                if self.health <= 0:
                    D.MEDIA['die_sound'].play()
                    self.kill()
                    self.toggle = True
            elif bullet.type == 'BIG_BULLET':
                self.health -= 2
                D.MEDIA['hit_sound'].play()
                if self.health <= 0:
                    D.MEDIA['die_sound'].play()
                    self.kill()
                    self.toggle = True
            elif bullet.type == 'LASER':
                self.health -= 1
                D.MEDIA['hit_sound'].play()
                if self.health <= 0:
                    D.MEDIA['die_sound'].play()
                    self.kill()
                    self.toggle = True
                else:
                    if bullet.vel[0] == 8 or -8 and bullet.vel[1] == 0:
                        self.pos[0] -= D.VEL_DICT['CONVERT']['LASER'][bullet.vel](bullet)
                    elif bullet.vel[1] == 8 or -8 and bullet.vel[0] == 0:
                        self.pos[1] -= D.VEL_DICT['CONVERT']['LASER'][bullet.vel](bullet)                   

# Bullet
class BULLET(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image, bullet_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = bullet_type
    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not G.PLAY_AREA.contains(self):
                self.kill()

# Red/Purple Laser Beam
class BEAM(pygame.sprite.Sprite):
    def __init__(self, pos, vel, color):
        super().__init__()
        self.color = color
        self.vel = (vel)
        self.image = D.VEL_DICT['COMPARE']['LASER_IMAGE'][self.color][self.vel]
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'LASER'
    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not G.PLAY_AREA.contains(self):
                self.kill()

# Green/Yellow Split Bullet
class SPLIT_BULLET(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image, groupa, groupb, color):
        super().__init__()
        self.color = color
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.vel = (vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'BULLET'
        self.groupa = groupa
        self.groupb = groupb
        self.alt_image = D.PLAYER_DICT[self.color]['BULLET_IMAGE']
    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not G.PLAY_AREA.contains(self):
                '''Runs ON_SPLIT Function, which creates three bullet instances and shoots them'''
                PARAMS = D.VEL_DICT['CONVERT']['SPLIT_BULLET'][self.vel]
                F.ON_SPLIT(self, D.MEDIA, self.groupa, self.groupb, *PARAMS)
                self.kill()

# Grey/White Reverse Bullet
class REVERSE_BULLET(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image, color):
        super().__init__()
        self.color = color
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.vel = (vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'BULLET'
        self.direction = D.VEL_DICT['CONVERT']['REVERSE_BULLET']['DIRECTION'][self.vel]
    def update(self):
        if self.toggle == False:
            # Using VEL_DICT, slowly decreases velocity and creates an arc
            self.vel = D.VEL_DICT['CONVERT']['REVERSE_BULLET'][self.color][self.direction](self)
            self.pos += self.vel
            self.rect.center = self.pos
            self.rect.center = self.pos
            if not G.PLAY_AREA.contains(self):
                self.kill()
    
# Selector
class SELECTOR(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = D.MEDIA['selector']
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(pos)
    def update(self):
        self.rect.center = self.pos
        if self.pos[0] > 470:
            self.pos[0] = 30
        elif self.pos[0] < 0:
            self.pos[0] = 470

# Larger Selector
class SELECTOR_BIG(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = D.MEDIA['selectorbig']
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(pos)
    def update(self):
        self.rect.center = self.pos
        if self.pos[1] > 350:
            self.pos[1] = 250
        elif self.pos[1] <= 150:
            self.pos[1] = 350
    
