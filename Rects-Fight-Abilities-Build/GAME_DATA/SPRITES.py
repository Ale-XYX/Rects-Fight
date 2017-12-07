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
            if bullet.type == 'BULLET':
                self.health -= 1
                m.MEDIA['hit_sound'].play()
                if self.health <= 0:
                    m.MEDIA['die_sound'].play()
                    self.kill()
                    self.toggle = True
            elif bullet.type == 'BIG_BULLET':
                self.health -= 2
                m.MEDIA['hit_sound'].play()
                if self.health <= 0:
                    m.MEDIA['die_sound'].play()
                    self.kill()
                    self.toggle = True
            elif bullet.type == 'LASER':
                self.health -= 1
                m.MEDIA['hit_sound'].play()
                if self.health <= 0:
                    m.MEDIA['die_sound'].play()
                    self.kill()
                    self.toggle = True
                else:
                    if bullet.vel[0] == 5 and bullet.vel[1] == 0:
                        self.pos[0] -= -(bullet.vel[0] + 10)
                    elif bullet.vel[0] == -5 and bullet.vel[1] == 0:
                        self.pos[0] -= -(bullet.vel[0] - 10)
                    elif bullet.vel[0] == 0 and bullet.vel[1] == 5:
                        self.pos[1] -= -(bullet.vel[1] + 10)
                    elif bullet.vel[0] == 0 and bullet.vel[1] == -5:
                        self.pos[1] -= -(bullet.vel[1] - 10)

# Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'BULLET'
    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not g.PLAY_AREA.contains(self):
                self.kill()
# Big Bullet [Blue/Orange Ability]

class BigBullet(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'BIG_BULLET'
    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not g.PLAY_AREA.contains(self):
                self.kill()
class RedBeam(pygame.sprite.Sprite):
    def __init__(self, pos, vel):
        super().__init__()
        if vel[0] == 0 and vel[1] == 5:
            self.image = pygame.transform.rotate(m.MEDIA['red_laser'], -90)
        elif vel[0] == 0 and vel[1] == -5:
            self.image = pygame.transform.rotate(m.MEDIA['red_laser'], 90)
        elif vel[0] == 5 and vel[1] == 0:
            self.image = m.MEDIA['red_laser']
        elif vel[0] == -5 and vel[1] == 0:
            self.image = m.MEDIA['red_laser']
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'LASER'
    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not g.PLAY_AREA.contains(self):
                self.kill()
                
class PurpleBeam(pygame.sprite.Sprite):
    def __init__(self, pos, vel):
        super().__init__()
        if vel[0] == 0 and vel[1] == 5:
            self.image = pygame.transform.rotate(m.MEDIA['purple_laser'], -90)
        elif vel[0] == 0 and vel[1] == -5:
            self.image = pygame.transform.rotate(m.MEDIA['purple_laser'], 90)
        elif vel[0] == 5 and vel[1] == 0:
            self.image = pygame.transform.flip(m.MEDIA['purple_laser'], True, False)
        elif vel[0] == -5 and vel[1] == 0:
            self.image = m.MEDIA['purple_laser']
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'LASER'
    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not g.PLAY_AREA.contains(self):
                self.kill()

class SplitBullet(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image, groupa, groupb, color):
        super().__init__()
        self.color = color
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'BULLET'
        self.groupa = groupa
        self.groupb = groupb
        self.alt_image = d.GAME_DICT[self.color]['BULLET_IMAGE']
    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not g.PLAY_AREA.contains(self):
                if self.vel[0] == 8 and self.vel[1] == 0:
                    bullet1 = Bullet(self.rect.center, (-8, 0), self.alt_image)
                    bullet2 = Bullet(self.rect.center, (-8, -5), self.alt_image)
                    bullet3 = Bullet(self.rect.center, (-8, 5), self.alt_image)
                    self.groupa.add(bullet1, bullet2, bullet3)
                    self.groupb.add(bullet1, bullet2, bullet3)
                    self.kill()
                if self.vel[0] == -8 and self.vel[1] == 0:
                    bullet1 = Bullet(self.rect.center, (8, 0), self.alt_image)
                    bullet2 = Bullet(self.rect.center, (8, -5), self.alt_image)
                    bullet3 = Bullet(self.rect.center, (8, 5), self.alt_image)
                    self.groupa.add(bullet1, bullet2, bullet3)
                    self.groupb.add(bullet1, bullet2, bullet3)
                    self.kill()                    
                if self.vel[0] == 0 and self.vel[1] == 8:
                    bullet1 = Bullet(self.rect.center, (0, -8), self.alt_image)
                    bullet2 = Bullet(self.rect.center, (5, -8), self.alt_image)
                    bullet3 = Bullet(self.rect.center, (-5, -8), self.alt_image)
                    self.groupa.add(bullet1, bullet2, bullet3)
                    self.groupb.add(bullet1, bullet2, bullet3)
                    self.kill()
                if self.vel[0] == 0 and self.vel[1] == -8:
                    bullet1 = Bullet(self.rect.center, (0, 8), self.alt_image)
                    bullet2 = Bullet(self.rect.center, (5, 8), self.alt_image)
                    bullet3 = Bullet(self.rect.center, (-5, 8), self.alt_image)
                    self.groupa.add(bullet1, bullet2, bullet3)
                    self.groupb.add(bullet1, bullet2, bullet3)
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
    
