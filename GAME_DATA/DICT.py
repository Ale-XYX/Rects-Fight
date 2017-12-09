# DICTIONARY
import GLOBAL as G
import SPRITES as S
import random
import pygame
import os
import glob

pygame.init()
pygame.mixer.init()

# Setting Up Items
MEDIA = {}
FILES = glob.glob(os.path.join(os.path.dirname(__file__), 'MEDIA_DATA', 'IMAGE', '*.png'))
FILES2 = glob.glob(os.path.join(os.path.dirname(__file__), 'MEDIA_DATA', 'AUDIO', '*.wav'))

# Loading images to use
for FILE_NAME in FILES:
    OBJ = pygame.image.load(FILE_NAME).convert_alpha()
    MEDIA[os.path.split(FILE_NAME)[-1][:-4]] = OBJ

# Loading audio to use
for FILE_NAME in FILES2:
    OBJ = pygame.mixer.Sound(FILE_NAME)
    MEDIA[os.path.split(FILE_NAME)[-1][:-4]] = OBJ
    
CLOCK = pygame.time.Clock()
# Sets up colors in a dictonary and returns a random color [For rainbow character]
def GET_RANDOM():
    i = random.randrange(0, 6)
    DICT = {
        0: G.BLUE,
        1: G.ORANGE,
        2: G.GREEN,
        3: G.PURPLE,
        4: G.RED,
        5: G.YELLOW,
        6: G.WHITE
    }
    return DICT[i]

# Blue/Orange Big bullet
def BIG_BULLET(GROUP_A, GROUP_B, POS, VEL, IMG, TYPE, DICTIONARY):
    VEL = DICTIONARY['VEL']['CONVERT']['BIG_BULLET'][VEL]        
    BIGBULLET = S.BULLET(POS, VEL, IMG, TYPE)
    GROUP_A.add(BIGBULLET)
    GROUP_B.add(BIGBULLET)
    MEDIA['big_shoot_sound'].play()

# Green/Yellow Split Bullet    
def SPLIT_BULLET(GROUP_A, GROUP_B, POS, VEL, IMG, COLOR):
    SPLIT_BULLET = S.SPLIT_BULLET(POS, VEL, IMG, GROUP_A, GROUP_B, COLOR)
    GROUP_A.add(SPLIT_BULLET)
    GROUP_B.add(SPLIT_BULLET)
    MEDIA['split_shoot_sound'].play()

# OnSplit Function
def ON_SPLIT(SELF, DICT, GROUP_A, GROUP_B, VEL_A, VEL_B, VEL_C):
    BULLET_A = S.BULLET(SELF.rect.center, VEL_A, SELF.alt_image, 'BULLET')
    BULLET_B = S.BULLET(SELF.rect.center, VEL_B, SELF.alt_image, 'BULLET')
    BULLET_C = S.BULLET(SELF.rect.center, VEL_C, SELF.alt_image, 'BULLET')
    GROUP_A.add(BULLET_A, BULLET_B, BULLET_C)
    GROUP_B.add(BULLET_A, BULLET_B, BULLET_C)
    DICT['bullet_split_sound'].play()    
    
# Red/Purple Laser Beam
def LASER_BEAM(GROUP_A, GROUP_B, POS, VEL, COLOR):
    BEAM = S.BEAM(POS, VEL, COLOR)
    GROUP_A.add(BEAM)
    GROUP_B.add(BEAM)
    MEDIA['laser_shoot_sound'].play()

# Grey/White reverse bullet        
def REVERSE_BULLET(GROUP_A, GROUP_B, POS, VEL, IMG, COLOR, DICTIONARY):
    VEL = DICTIONARY['VEL']['CONVERT']['REVERSE_BULLET']['VEL'][VEL]
    REVERSE_BULLET = S.REVERSE_BULLET(POS, VEL, IMG, COLOR)
    GROUP_A.add(REVERSE_BULLET)
    GROUP_B.add(REVERSE_BULLET)
    MEDIA['reverse_shoot_sound'].play()
    
# Rainbow Multi-bullet
def MULTI_BULLET(GROUP_A, GROUP_B, POS):
    BULLET_1 = S.BULLET(POS, (6, 0), MEDIA['red_bullet'], 'BULLET')
    BULLET_2 = S.BULLET(POS, (6, -6), MEDIA['orange_bullet'], 'BULLET')
    BULLET_3 = S.BULLET(POS, (0, -6), MEDIA['yellow_bullet'], 'BULLET')
    BULLET_4 = S.BULLET(POS, (-6, -6), MEDIA['green_bullet'], 'BULLET')
    BULLET_5 = S.BULLET(POS, (-6, 0), MEDIA['blue_bullet'], 'BULLET')
    BULLET_6 = S.BULLET(POS, (-6, 6), MEDIA['purple_bullet'], 'BULLET')
    BULLET_7 = S.BULLET(POS, (0, 6), MEDIA['white_bullet'], 'BULLET')
    BULLET_8 = S.BULLET(POS, (6, 6), MEDIA['grey_bullet'], 'BULLET')
    GROUP_A.add(BULLET_1, BULLET_2, BULLET_3, BULLET_4, BULLET_5, BULLET_6, BULLET_7, BULLET_8)
    GROUP_B.add(BULLET_1, BULLET_2, BULLET_3, BULLET_4, BULLET_5, BULLET_6, BULLET_7, BULLET_8)
    MEDIA['multi_shoot_sound'].play()      

GAME_DICT = {
    # Player Media, Colors, And Locations
    'BLUE': {
        'COLOR': G.BLUE,
        'PLAYER_IMAGE': MEDIA['blue_face'],
        'BULLET_IMAGE': MEDIA['blue_bullet'],
        'LOCAL': 220,
        'ABILITY': BIG_BULLET},
    'ORANGE': {
        'COLOR': G.ORANGE,
        'PLAYER_IMAGE': MEDIA['orange_face'],
        'BULLET_IMAGE': MEDIA['orange_bullet'],
        'LOCAL': 220,
        'ABILITY': BIG_BULLET},
    'GREEN': {
        'COLOR': G.GREEN,
        'PLAYER_IMAGE': MEDIA['green_face'],
        'BULLET_IMAGE': MEDIA['green_bullet'],
        'LOCAL': 210,
        'ABILITY': SPLIT_BULLET,
        'SPLIT_BULLET_IMAGE': MEDIA['green_split_bullet']},
    'PURPLE': {
        'COLOR': G.PURPLE,
        'PLAYER_IMAGE': MEDIA['purple_face'],
        'BULLET_IMAGE': MEDIA['purple_bullet'],
        'LOCAL': 210,
        'ABILITY': LASER_BEAM},
    'RED': {
        'COLOR': G.RED,
        'PLAYER_IMAGE': MEDIA['red_face'],
        'BULLET_IMAGE': MEDIA['red_bullet'],
        'LOCAL': 224,
        'ABILITY': LASER_BEAM},
    'YELLOW': {
        'COLOR': G.YELLOW,
        'PLAYER_IMAGE': MEDIA['yellow_face'],
        'BULLET_IMAGE': MEDIA['yellow_bullet'],
        'LOCAL': 209,
        'ABILITY': SPLIT_BULLET,
        'SPLIT_BULLET_IMAGE': MEDIA['yellow_split_bullet']},
    'GREY': {
        'COLOR': G.GREY,
        'PLAYER_IMAGE': MEDIA['grey_face'],
        'BULLET_IMAGE': MEDIA['grey_bullet'],
        'LOCAL': 220,
        'ABILITY': REVERSE_BULLET},
    'WHITE': {
        'COLOR': G.WHITE,
        'PLAYER_IMAGE': MEDIA['white_face'],
        'BULLET_IMAGE': MEDIA['white_bullet'],
        'LOCAL': 210,
        'ABILITY': REVERSE_BULLET},
    'RAINBOW': {
        'COLOR': GET_RANDOM(),
        'PLAYER_IMAGE': MEDIA['rainbow_face'],
        'BULLET_IMAGE': MEDIA['rainbow_bullet'],
        'LOCAL': 190,
        'ABILITY': MULTI_BULLET},
    # HP Bars
    'HP': {
        0: MEDIA['hp_dead'],
        1: MEDIA['hp_low'],
        2: MEDIA['hp_decayed'],
        3: MEDIA['hp_full'],
        -1: MEDIA['hp_dead']},
    # Mode Values [Loaded In main game depending on G.MODE]
    'MODE': {
        'CLASSIC': {
            'TIMER': 30,
            'PLAYER_VELOCITY': 6,
            'BULLET_VELOCITY': 8,
            'HEALTH': 3,
            'SOUND': MEDIA['classic_sound'],
            'MUSIC': MEDIA['classic_music'],
            'DT': CLOCK.tick(60) / 1000},
        'CHAOS': {
            'TIMER': 10,
            'PLAYER_VELOCITY': 8,
            'BULLET_VELOCITY': 16,
            'HEALTH': 1,
            'SOUND': MEDIA['chaos_sound'], 
            'MUSIC': MEDIA['chaos_music'],
            'DT': CLOCK.tick(60) / 100}
        },
    # Timer Values
    'TIMER': {
        True: [G.RED, G.FONTB],
        False: [G.WHITE, G.FONTNORMAL]},
    'VEL': {
        'CONVERT': {
            'BIG_BULLET': {
                (8, 0): (4, 0),
                (-8, 0): (-4, 0),
                (0, 8): (0, 4),
                (0, -8): (0, -4),
                (16, 0): (8, 0),
                (-16, 0): (-8, 0),
                (0, 16): (0, 8),
                (0, -16): (0, -8)},
            'LASER': {
                (8, 0): lambda bullet: -(bullet.vel[0] + 10),
                (-8, 0): lambda bullet: -(bullet.vel[0] - 10),
                (0, 8): lambda bullet: -(bullet.vel[1] + 10),
                (0, -8): lambda bullet: -(bullet.vel[1] - 10),
                (16, 0): lambda bullet: -(bullet.vel[0] + 20),
                (-16, 0): lambda bullet: -(bullet.vel[0] - 20),
                (0, 16): lambda bullet: -(bullet.vel[1] + 20),
                (0, -16): lambda bullet: -(bullet.vel[1] - 20)},
            'SPLIT_BULLET': {
                (8, 0): [(-8, 0), (-8, -5), (-8, 5)],
                (-8, 0): [(8, 0), (8, -5), (8, 5)],
                (0, 8): [(0, -8), (5, -8), (-5, -8)],
                (0, -8): [(0, 8), (5, 8), (-5, 8)],
                (16, 0): [(-16, 10), (-16, -10), (-16, 10)],
                (-16, 0): [(16, 0), (16, -10), (16, 10)],
                (0, 16): [(0, -16), (10, -16), (-10, -16)],
                (0, -16): [(0, 16), (10, 16), (-10, 16)]},
            'REVERSE_BULLET': {
                'VEL': {
                    (8, 0): (8, 0),
                    (-8, 0): (-8, 0),
                    (0, 8): (0, 8),
                    (0, -8): (0, -8),
                    (16, 0): (12, 0),
                    (-16, 0): (-12, 0),
                    (0, 16): (0, 12),
                    (0, -16): (0, -12)},
                'DIRECTION': {
                    (8, 0): 'RIGHT',
                    (-8, 0): 'LEFT',
                    (0, 8): 'DOWN',
                    (0, -8): 'UP',
                    (12, 0): 'RIGHT',
                    (-12, 0): 'LEFT',
                    (0, 12): 'DOWN',
                    (0, -12): 'UP'},
                'WHITE': {
                    'RIGHT': lambda self: (self.vel[0] - 0.2, self.vel[1] - 0.02),
                    'LEFT': lambda self: (self.vel[0] + 0.2, self.vel[1] + 0.02),
                    'UP': lambda self: (self.vel[0] - 0.02, self.vel[1] + 0.2),
                    'DOWN': lambda self: (self.vel[0] - 0.02, self.vel[1] - 0.2)},
                'GREY': {
                    'RIGHT': lambda self: (self.vel[0] - 0.2, self.vel[1] + 0.02),
                    'LEFT': lambda self: (self.vel[0] + 0.2, self.vel[1] - 0.02),
                    'UP': lambda self: (self.vel[0] + 0.02, self.vel[1] + 0.2),
                    'DOWN': lambda self:(self.vel[0] + 0.02, self.vel[1] - 0.2)}
                }
            },
        'COMPARE': {
            'LASER_IMAGE': {
                'PURPLE': {
                    (8, 0): MEDIA['purple_laser'],
                    (-8, 0): MEDIA['purple_laser'],
                    (0, 8): pygame.transform.rotate(MEDIA['purple_laser'], -90),
                    (0, -8): pygame.transform.rotate(MEDIA['purple_laser'], 90),
                    (16, 0): MEDIA['purple_laser'],
                    (-16, 0): MEDIA['purple_laser'],
                    (0, 16): pygame.transform.rotate(MEDIA['purple_laser'], -90),
                    (0, -16): pygame.transform.rotate(MEDIA['purple_laser'], 90)},
                'RED': {
                    (8, 0): MEDIA['red_laser'],
                    (-8, 0): MEDIA['red_laser'],
                    (0, 8): pygame.transform.rotate(MEDIA['red_laser'], -90),
                    (0, -8): pygame.transform.rotate(MEDIA['red_laser'], 90),
                    (16, 0): MEDIA['red_laser'],
                    (-16, 0): MEDIA['red_laser'],
                    (0, 16): pygame.transform.rotate(MEDIA['red_laser'], -90),
                    (0, -16): pygame.transform.rotate(MEDIA['red_laser'], 90)},                    
                }
            }
        }
    }

