# DICTIONARY
import GLOBAL as G
import SPRITES as S
import random
import pygame
import os
import glob

pygame.init()
pygame.mixer.init()

CLOCK = pygame.time.Clock()

# Media Dictionary
# Loads sounds/images into dictionary based on filename
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
    

# Player Media Dictionary
# When accsessed, returns images for characters
PLAYER_DICT = {
    'BLUE': {
        'COLOR': G.BLUE,
        'PLAYER_IMAGE': MEDIA['blue_face'],
        'BULLET_IMAGE': MEDIA['blue_bullet'],
        'LOCAL': 220,
        'PARAMS': [MEDIA['blue_big_bullet'], 'BIG_BULLET']},
    'ORANGE': {
        'COLOR': G.ORANGE,
        'PLAYER_IMAGE': MEDIA['orange_face'],
        'BULLET_IMAGE': MEDIA['orange_bullet'],
        'LOCAL': 220,
        'PARAMS': [MEDIA['orange_big_bullet'], 'BIG_BULLET']},
    'GREEN': {
        'COLOR': G.GREEN,
        'PLAYER_IMAGE': MEDIA['green_face'],
        'BULLET_IMAGE': MEDIA['green_bullet'],
        'LOCAL': 210,
        'SPLIT_BULLET_IMAGE': MEDIA['green_split_bullet'],
        'PARAMS': [MEDIA['green_split_bullet'], 'GREEN']},
    'YELLOW': {
        'COLOR': G.YELLOW,
        'PLAYER_IMAGE': MEDIA['yellow_face'],
        'BULLET_IMAGE': MEDIA['yellow_bullet'],
        'LOCAL': 209,
        'SPLIT_BULLET_IMAGE': MEDIA['yellow_split_bullet'],
        'PARAMS': [MEDIA['yellow_split_bullet'], 'YELLOW']},
    'PURPLE': {
        'COLOR': G.PURPLE,
        'PLAYER_IMAGE': MEDIA['purple_face'],
        'BULLET_IMAGE': MEDIA['purple_bullet'],
        'LOCAL': 210,
        'PARAMS': ['PURPLE']},
    'RED': {
        'COLOR': G.RED,
        'PLAYER_IMAGE': MEDIA['red_face'],
        'BULLET_IMAGE': MEDIA['red_bullet'],
        'LOCAL': 224,
        'PARAMS': ['RED']
        },
    'GREY': {
        'COLOR': G.GREY,
        'PLAYER_IMAGE': MEDIA['grey_face'],
        'BULLET_IMAGE': MEDIA['grey_bullet'],
        'LOCAL': 220,
        'PARAMS': [MEDIA['grey_boomerang_bullet'], 'GREY']},
    'WHITE': {
        'COLOR': G.WHITE,
        'PLAYER_IMAGE': MEDIA['white_face'],
        'BULLET_IMAGE': MEDIA['white_bullet'],
        'LOCAL': 210,
        'PARAMS': [MEDIA['white_boomerang_bullet'], 'WHITE']},
    'RAINBOW': {
        'COLOR': random.choice((G.BLUE, G.ORANGE, G.GREEN, G.PURPLE, G.RED, G.YELLOW, G.WHITE)),
        'PLAYER_IMAGE': MEDIA['rainbow_face'],
        'BULLET_IMAGE': MEDIA['rainbow_bullet'],
        'LOCAL': 190,
        'PARAMS': ['PLACEHOLDER']},
    }

# Velocity Dictionary
# Converts and compares velocities (for abilities)
VEL_DICT = {
    'CONVERT': {
        'BIG_BULLET': {
            (8, 0): (4, 0),
            (-8, 0): (-4, 0),
            (0, 8): (0, 4),
            (0, -8): (0, -4),

            (12, 0): (6, 0),
            (-12, 0): (-6, 0),
            (0, 12): (0, 6),
            (0, -12): (0, -6),
            
            (16, 0): (8, 0),
            (-16, 0): (-8, 0),
            (0, 16): (0, 8),
            (0, -16): (0, -8)},
        'LASER': {
            (8, 0): lambda bullet: -(bullet.vel[0] + 10),
            (-8, 0): lambda bullet: -(bullet.vel[0] - 10),
            (0, 8): lambda bullet: -(bullet.vel[1] + 10),
            (0, -8): lambda bullet: -(bullet.vel[1] - 10),
            
            (12, 0): lambda bullet: -(bullet.vel[0] + 15),
            (-12, 0): lambda bullet: -(bullet.vel[0] - 15),
            (0, 12): lambda bullet: -(bullet.vel[1] + 15),
            (0, -12): lambda bullet: -(bullet.vel[1] - 15),
            
            (16, 0): lambda bullet: -(bullet.vel[0] + 20),
            (-16, 0): lambda bullet: -(bullet.vel[0] - 20),
            (0, 16): lambda bullet: -(bullet.vel[1] + 20),
            (0, -16): lambda bullet: -(bullet.vel[1] - 20)},
        'SPLIT_BULLET': {
            (8, 0): [(-8, 0), (-8, -5), (-8, 5)],
            (-8, 0): [(8, 0), (8, -5), (8, 5)],
            (0, 8): [(0, -8), (5, -8), (-5, -8)],
            (0, -8): [(0, 8), (5, 8), (-5, 8)],

            (12, 0): [(-12, 0), (-12, -8), (-12, 8)],
            (-12, 0): [(12, 0), (12, -8), (12, 8)],
            (0, 12): [(0, -12), (8, -12), (-8, -12)],
            (0, -12): [(0, 12), (8, 12), (-8, 12)],
        
            (16, 0): [(-16, 0), (-16, -10), (-16, 10)],
            (-16, 0): [(16, 0), (16, -10), (16, 10)],
            (0, 16): [(0, -16), (10, -16), (-10, -16)],
            (0, -16): [(0, 16), (10, 16), (-10, 16)]},
        'REVERSE_BULLET': {
            'VEL': {
                (8, 0): (8, 0),
                (-8, 0): (-8, 0),
                (0, 8): (0, 8),
                (0, -8): (0, -8),
                (12, 0): (10, 0),
                (-12, 0): (-10, 0),
                (0, 12): (0, 10),
                (0, -12): (0, -10),              
                (16, 0): (12, 0),
                (-16, 0): (-12, 0),
                (0, 16): (0, 12),
                (0, -16): (0, -12)},
            'DIRECTION': {
                (8, 0): 'RIGHT',
                (-8, 0): 'LEFT',
                (0, 8): 'DOWN',
                (0, -8): 'UP',
                (10, 0): 'MEDRIGHT',
                (-10, 0): 'MEDLEFT',
                (0, 10): 'MEDDOWN',
                (0, -10): 'MEDUP',
                (12, 0): 'FASTRIGHT',
                (-12, 0): 'FASTLEFT',
                (0, 12): 'FASTDOWN',
                (0, -12): 'FASTUP'},
            'WHITE': {
                'RIGHT': lambda self: (self.vel[0] - 0.2, self.vel[1] - 0.02),
                'LEFT': lambda self: (self.vel[0] + 0.2, self.vel[1] + 0.02),
                'UP': lambda self: (self.vel[0] - 0.02, self.vel[1] + 0.2),
                'DOWN': lambda self: (self.vel[0] + 0.02, self.vel[1] - 0.2),
                
                'MEDRIGHT': lambda self: (self.vel[0] - 0.4, self.vel[1] - 0.1),
                'MEDLEFT': lambda self: (self.vel[0] + 0.4, self.vel[1] + 0.1),
                'MEDUP': lambda self: (self.vel[0] - 0.1, self.vel[1] + 0.4),
                'MEDDOWN': lambda self: (self.vel[0] + 0.1, self.vel[1] - 0.4),
                
                'FASTRIGHT': lambda self: (self.vel[0] - 0.6, self.vel[1] - 0.15),
                'FASTLEFT': lambda self: (self.vel[0] + 0.6, self.vel[1] + 0.15),
                'FASTUP': lambda self: (self.vel[0] - 0.15, self.vel[1] + 0.6),
                'FASTDOWN': lambda self: (self.vel[0] + 0.15, self.vel[1] - 0.6)},
            'GREY': {
                'RIGHT': lambda self: (self.vel[0] - 0.2, self.vel[1] + 0.02),
                'LEFT': lambda self: (self.vel[0] + 0.2, self.vel[1] - 0.02),
                'UP': lambda self: (self.vel[0] + 0.02, self.vel[1] + 0.2),
                'DOWN': lambda self:(self.vel[0] - 0.02, self.vel[1] - 0.2),
                
                'MEDRIGHT': lambda self: (self.vel[0] - 0.4, self.vel[1] + 0.1),
                'MEDLEFT': lambda self: (self.vel[0] + 0.4, self.vel[1] - 0.1),
                'MEDUP': lambda self: (self.vel[0] + 0.1, self.vel[1] + 0.4),
                'MEDDOWN': lambda self: (self.vel[0] - 0.1, self.vel[1] - 0.4),
                
                'FASTRIGHT': lambda self: (self.vel[0] - 0.6, self.vel[1] + 0.15),
                'FASTLEFT': lambda self: (self.vel[0] + 0.6, self.vel[1] - 0.15),
                'FASTUP': lambda self: (self.vel[0] + 0.15, self.vel[1] + 0.6),
                'FASTDOWN': lambda self:(self.vel[0] - 0.15, self.vel[1] - 0.6)}
            },
        'MULTI_BULLET': {
            'CLASSIC': {
                1: (5, 0),
                2: (5, -5),
                3: (0, -5),
                4: (-5, -5),
                5: (-5, 0),
                6: (-5, 5),
                7: (0, 5),
                8: (5, 5)
                },
            'TENSE': {
                1: (7, 0),
                2: (7, -7),
                3: (0, -7),
                4: (-7, -7),
                5: (-7, 0),
                6: (-7, 7),
                7: (0, 7),
                8: (7, 7)
                },
            'CHAOS': {
                1: (9, 0),
                2: (9, -9),
                3: (0, -9),
                4: (-9, -9),
                5: (-9, 0),
                6: (-9, 9),
                7: (0, 9),
                8: (9, 9)
                },
            None: {
                1: (5, 0),
                2: (5, -5),
                3: (0, -5),
                4: (-5, -5),
                5: (-5, 0),
                6: (-5, 5),
                7: (0, 5),
                8: (5, 5)
                },
            }
        },
    'COMPARE': {
        'LASER_IMAGE': {
            'PURPLE': {
                (8, 0): MEDIA['purple_laser'],
                (-8, 0): MEDIA['purple_laser'],
                (0, 8): pygame.transform.rotate(MEDIA['purple_laser'], -90),
                (0, -8): pygame.transform.rotate(MEDIA['purple_laser'], 90),
                
                (12, 0): MEDIA['purple_laser'],
                (-12, 0): MEDIA['purple_laser'],
                (0, 12): pygame.transform.rotate(MEDIA['purple_laser'], -90),
                (0, -12): pygame.transform.rotate(MEDIA['purple_laser'], 90),
                                                  
                (16, 0): MEDIA['purple_laser'],
                (-16, 0): MEDIA['purple_laser'],
                (0, 16): pygame.transform.rotate(MEDIA['purple_laser'], -90),
                (0, -16): pygame.transform.rotate(MEDIA['purple_laser'], 90)},
            'RED': {
                (8, 0): MEDIA['red_laser'],
                (-8, 0): MEDIA['red_laser'],
                (0, 8): pygame.transform.rotate(MEDIA['red_laser'], -90),
                (0, -8): pygame.transform.rotate(MEDIA['red_laser'], 90),

                (12, 0): MEDIA['red_laser'],
                (-12, 0): MEDIA['red_laser'],
                (0, 12): pygame.transform.rotate(MEDIA['red_laser'], -90),
                (0, -12): pygame.transform.rotate(MEDIA['red_laser'], 90),
                
                (16, 0): MEDIA['red_laser'],
                (-16, 0): MEDIA['red_laser'],
                (0, 16): pygame.transform.rotate(MEDIA['red_laser'], -90),
                (0, -16): pygame.transform.rotate(MEDIA['red_laser'], 90)},                    
            }
        }
    }

# Mode Values
# Values are accsessed based on G.MODE]
MODE_DICT = {
    'CLASSIC': {
        'TIMER': 30,
        'PLAYER_VELOCITY': 6,
        'BULLET_VELOCITY': 8,
        'HEALTH': 3,
        'SOUND': MEDIA['classic_sound'],
        'MUSIC': MEDIA['classic_music'],
        'COOLDOWN': 3},
    'TENSE': {
        'TIMER': 20,
        'PLAYER_VELOCITY': 7,
        'BULLET_VELOCITY': 12,
        'HEALTH': 2,
        'SOUND': MEDIA['tense_sound'],
        'MUSIC': MEDIA['tense_music'],
        'COOLDOWN': 1},
    'CHAOS': {
        'TIMER': 10,
        'PLAYER_VELOCITY': 8,
        'BULLET_VELOCITY': 16,
        'HEALTH': 1,
        'SOUND': MEDIA['chaos_sound'], 
        'MUSIC': MEDIA['chaos_music'],
        'COOLDOWN': 0.3}
    }

# HP Bars
# Works like PLAYER_DICT, but with player.health
HP_DICT = {
    0: MEDIA['hp_dead'],
    1: MEDIA['hp_low'],
    2: MEDIA['hp_decayed'],
    3: MEDIA['hp_full'],
    -1: MEDIA['hp_dead']
    }

# Timer
# Works as HP bars and player_dict
TIMER_DICT = {
    True: [G.RED, G.FONTB],
    False: [G.WHITE, G.FONTNORMAL]
    }
    
