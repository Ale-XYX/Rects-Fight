import pygame
import DICTIONARY as D
import GLOBAL as G

# Ability Functions
# First converts velocities, then creates bullet instances and spawns them.
def BIG_BULLET(GROUP_A, GROUP_B, POS, VEL, IMG, TYPE):
    VEL = D.VEL_DICT['CONVERT']['BIG_BULLET'][VEL]        
    BIGBULLET = D.S.BULLET(POS, VEL, IMG, TYPE)
    GROUP_A.add(BIGBULLET)
    GROUP_B.add(BIGBULLET)
    D.MEDIA['big_shoot_sound'].play()
    
def SPLIT_BULLET(GROUP_A, GROUP_B, POS, VEL, IMG, COLOR):
    SPLIT_BULLET = D.S.SPLIT_BULLET(POS, VEL, IMG, GROUP_A, GROUP_B, COLOR)
    GROUP_A.add(SPLIT_BULLET)
    GROUP_B.add(SPLIT_BULLET)
    D.MEDIA['split_shoot_sound'].play()

def ON_SPLIT(SELF, DICT, GROUP_A, GROUP_B, VEL_A, VEL_B, VEL_C):
    BULLET_A = D.S.BULLET(SELF.rect.center, VEL_A, SELF.alt_image, 'BULLET')
    BULLET_B = D.S.BULLET(SELF.rect.center, VEL_B, SELF.alt_image, 'BULLET')
    BULLET_C = D.S.BULLET(SELF.rect.center, VEL_C, SELF.alt_image, 'BULLET')
    GROUP_A.add(BULLET_A, BULLET_B, BULLET_C)
    GROUP_B.add(BULLET_A, BULLET_B, BULLET_C)
    D.MEDIA['bullet_split_sound'].play()   

def LASER_BEAM(GROUP_A, GROUP_B, POS, VEL, COLOR):
    BEAM = D.S.BEAM(POS, VEL, COLOR)
    GROUP_A.add(BEAM)
    GROUP_B.add(BEAM)
    D.MEDIA['laser_shoot_sound'].play()
        
def REVERSE_BULLET(GROUP_A, GROUP_B, POS, VEL, IMG, COLOR):
    VEL = D.VEL_DICT['CONVERT']['REVERSE_BULLET']['VEL'][VEL]
    REVERSE_BULLET = D.S.REVERSE_BULLET(POS, VEL, IMG, COLOR)
    GROUP_A.add(REVERSE_BULLET)
    GROUP_B.add(REVERSE_BULLET)
    D.MEDIA['reverse_shoot_sound'].play()

def MULTI_BULLET(GROUP_A, GROUP_B, POS, FIRE_DIRECTION, PLACEHOLDER):
    BULLET_1 = D.S.BULLET(POS, D.VEL_DICT['CONVERT']['MULTI_BULLET'][G.MODE][1], D.MEDIA['red_bullet'], 'BULLET')
    BULLET_2 = D.S.BULLET(POS, D.VEL_DICT['CONVERT']['MULTI_BULLET'][G.MODE][2], D.MEDIA['orange_bullet'], 'BULLET')
    BULLET_3 = D.S.BULLET(POS, D.VEL_DICT['CONVERT']['MULTI_BULLET'][G.MODE][3], D.MEDIA['yellow_bullet'], 'BULLET')
    BULLET_4 = D.S.BULLET(POS, D.VEL_DICT['CONVERT']['MULTI_BULLET'][G.MODE][4], D.MEDIA['green_bullet'], 'BULLET')
    BULLET_5 = D.S.BULLET(POS, D.VEL_DICT['CONVERT']['MULTI_BULLET'][G.MODE][5], D.MEDIA['blue_bullet'], 'BULLET')
    BULLET_6 = D.S.BULLET(POS, D.VEL_DICT['CONVERT']['MULTI_BULLET'][G.MODE][6], D.MEDIA['purple_bullet'], 'BULLET')
    BULLET_7 = D.S.BULLET(POS, D.VEL_DICT['CONVERT']['MULTI_BULLET'][G.MODE][7], D.MEDIA['white_bullet'], 'BULLET')
    BULLET_8 = D.S.BULLET(POS, D.VEL_DICT['CONVERT']['MULTI_BULLET'][G.MODE][8], D.MEDIA['grey_bullet'], 'BULLET')
    GROUP_A.add(BULLET_1, BULLET_2, BULLET_3, BULLET_4, BULLET_5, BULLET_6, BULLET_7, BULLET_8)
    GROUP_B.add(BULLET_1, BULLET_2, BULLET_3, BULLET_4, BULLET_5, BULLET_6, BULLET_7, BULLET_8)
    D.MEDIA['multi_shoot_sound'].play()

# Check mode and then returns images
# Yes, I could use an dictionary for it but its not instant
def GET_COOLDOWN_IMG(MODE, COOLDOWN):
    if MODE == 'CLASSIC':
        if COOLDOWN <= 3 and COOLDOWN >= 2:
            return D.MEDIA['cooldown4']
        elif COOLDOWN <= 2 and COOLDOWN >= 1:
            return D.MEDIA['cooldown3']
        elif COOLDOWN <= 1 and COOLDOWN >= 0:
            return D.MEDIA['cooldown2']
        elif COOLDOWN <= 0:
            return D.MEDIA['cooldown1']
    elif MODE == 'TENSE':
        if COOLDOWN <= 1 and COOLDOWN >= 0.6:
            return D.MEDIA['cooldown4']
        elif COOLDOWN <= 0.6 and COOLDOWN >= 0.3:
            return D.MEDIA['cooldown3']
        elif COOLDOWN <= 0.3 and COOLDOWN >= 0:
            return D.MEDIA['cooldown2']
        elif COOLDOWN <= 0:
            return D.MEDIA['cooldown1']         
    elif MODE == 'CHAOS':
        if COOLDOWN <= 0.3 and COOLDOWN >= 0.2:
            return D.MEDIA['cooldown4']
        elif COOLDOWN <= 0.2 and COOLDOWN >= 0.1:
            return D.MEDIA['cooldown3']
        elif COOLDOWN <= 0.1 and COOLDOWN >= 0:
            return D.MEDIA['cooldown2']
        elif COOLDOWN <= 0:
            return D.MEDIA['cooldown1']

    
