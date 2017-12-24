import pygame
import globals
import dictionaries

def on_split(self, group_a, group_b, vel_a, vel_b, vel_c):
    bullet_a = Bullet(self.rect.center, vel_a, self.alt_image, 'Bullet')
    bullet_b = Bullet(self.rect.center, vel_b, self.alt_image, 'Bullet')
    bullet_c = Bullet(self.rect.center, vel_c, self.alt_image, 'Bullet')
    group_a.add(bullet_a, bullet_b, bullet_c)
    group_b.add(bullet_a, bullet_b, bullet_c)
    dictionaries.MEDIA['bullet_split_sound'].play()


class RectPlayer(pygame.sprite.Sprite):
    def __init__(self, pos, enemy_bullets, direction, color, ability, *groups):
        super().__init__(*groups)
        self.image = dictionaries.PLAYER_MEDIA[color]['Image']
        self.color = dictionaries.PLAYER_MEDIA[color]['Color']
        self.bullet_image = dictionaries.PLAYER_MEDIA[color]['Bullet_Image']
        self.params = dictionaries.PLAYER_MEDIA[color]['Parameters']
        self.ability = ability
        self.rect = self.image.get_rect(center=pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)
        self.fire_direction = direction
        self.health = 3
        self.enemy_bullets = enemy_bullets
        self.toggle = False

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        self.rect.clamp_ip(globals.playarea)
        collided = pygame.sprite.spritecollide(self, self.enemy_bullets, True)

        for bullet in collided:
            if bullet.type == 'Bullet':
                self.health -= 1
                dictionaries.MEDIA['hit_sound'].play()
                if self.health == 0:
                    dictionaries.MEDIA['die_sound'].play()
                    self.kill()
                    self.toggle = True
            elif bullet.type == 'Big_Bullet':
                print('Test')
                self.health -= 2
                dictionaries.MEDIA['hit_sound'].play()
                if self.health <= 0:
                    dictionaries.MEDIA['die_sound'].play()
                    self.kill()
                    self.toggle = True
            elif bullet.type == 'Laser':
                self.health -= 1
                dictionaries.MEDIA['hit_sound'].play()
                if self.health <= 0:
                    dictionaries.MEDIA['die_sound'].play()
                    self.kill()
                    self.toggle = True
                else:
                    if bullet.vel[0] == 8 or -8 and bullet.vel[1] == 0:
                        self.pos[0] -= dictionaries.VELOCITY_VALUES['Convert']['Laser'][bullet.vel](bullet)
                    elif bullet.vel[1] == 8 or -8 and bullet.vel[0] == 0:
                        self.pos[1] -= dictionaries.VELOCITY_VALUES['Convert']['Laser'][bullet.vel](bullet)


# Basic bullet [All, is used for big_bullet]
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image, bullet_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.vel = pygame.math.Vector2(vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = bullet_type

    def update(self):
        if self.toggle is False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not globals.playarea.contains(self):
                self.kill()


# Beam [Red/Purple]
class Beam(pygame.sprite.Sprite):
    def __init__(self, pos, vel, color):
        super().__init__()
        self.color = color
        self.vel = vel
        self.image = dictionaries.VELOCITY_VALUES['Compare']['Laser_Image'][self.color][self.vel]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'Laser'

    def update(self):
        if self.toggle is False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not globals.playarea.contains(self):
                self.kill()


# Split Bullet [Green/Yellow]
class SplitBullet(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image, group_a, group_b, color):
        super().__init__()
        self.color = color
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.vel = vel
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'Bullet'
        self.group_a = group_a
        self.group_b = group_b
        self.alt_image = dictionaries.PLAYER_MEDIA[self.color]['Bullet_Image']

    def update(self):
        if self.toggle is False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not globals.playarea.contains(self):
                v_parameters = dictionaries.VELOCITY_VALUES['Convert']['Split_Bullet'][self.vel]
                on_split(self, self.group_a, self.group_b, *v_parameters)
                self.kill()


# Reverse bullet [Grey/White]
class ReverseBullet(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image, color):
        super().__init__()
        self.color = color
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.vel = vel
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
        self.type = 'Bullet'
        self.direction = dictionaries.VELOCITY_VALUES['Convert']['Reverse_Bullet']['Direction'][self.vel]

    def update(self):
        if self.toggle is False:
            # Using VEL_DICT, slowly decreases velocity and creates an arc
            self.vel = dictionaries.VELOCITY_VALUES['Convert']['Reverse_Bullet'][self.color][self.direction](self)
            self.pos += self.vel
            self.rect.center = self.pos
            self.rect.center = self.pos
            if not globals.playarea.contains(self):
                self.kill()


# Selector
class Selector(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = dictionaries.MEDIA['selector']
        self.rect = self.image.get_rect(center=pos)
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
        self.image = dictionaries.MEDIA['selectorbig']
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)

    def update(self):
        self.rect.center = self.pos
        if self.pos[1] >= 500:
            self.pos[1] = 200
        elif self.pos[1] <= 100:
            self.pos[1] = 400