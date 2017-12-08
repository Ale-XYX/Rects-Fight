# DICTIONARY
import MEDIA as m
import GLOBAL as g
import SPRITES as s
import random
import pygame

CLOCK = pygame.time.Clock()
# Sets up colors in a dictonary and returns a random color [For rainbow character]
def GET_RANDOM():
    i = random.randrange(0, 6)
    DICT = {
        0: g.BLUE,
        1: g.ORANGE,
        2: g.GREEN,
        3: g.PURPLE,
        4: g.RED,
        5: g.YELLOW,
        6: g.WHITE
    }
    return DICT[i]

# Blue/Orange Big bullet
def BIG_BULLET(GROUP_A, GROUP_B, POS, VEL, IMG):
    if VEL[0] == 8 and VEL[1] == 0:
        VEL = (VEL[0] - 4, 0)
    elif VEL[0] == -8 and VEL[1] == 0:
        VEL = (VEL[0] + 4, 0)
    elif VEL[0] == 0 and VEL[1] == 8:
        VEL = (0, VEL[1] - 4)
    elif VEL[0] == 0 and VEL[1] == -8:
        VEL = (0, VEL[1] + 4)
    BIGBULLET = s.BIG_BULLET(POS, VEL, IMG)
    GROUP_A.add(BIGBULLET)
    GROUP_B.add(BIGBULLET)
    m.MEDIA['big_shoot_sound'].play()

# Green/Yellow Split Bullet    
def SPLIT_BULLET(GROUP_A, GROUP_B, POS, VEL, IMG, COLOR):
    SPLIT_BULLET = s.SPLIT_BULLET(POS, VEL, IMG, GROUP_A, GROUP_B, COLOR)
    GROUP_A.add(SPLIT_BULLET)
    GROUP_B.add(SPLIT_BULLET)
    m.MEDIA['split_shoot_sound'].play()
    
# Red/Purple Laser Beam
def LASER_BEAM(GROUP_A, GROUP_B, POS, VEL, COLOR):
    BEAM = s.BEAM(POS, VEL, COLOR)
    GROUP_A.add(BEAM)
    GROUP_B.add(BEAM)
    m.MEDIA['laser_shoot_sound'].play()

# Grey/White reverse bullet        
def REVERSE_BULLET(GROUP_A, GROUP_B, POS, VEL, IMG):
    REVERSE_BULLET = s.REVERSE_BULLET(POS, VEL, IMG)
    GROUP_A.add(REVERSE_BULLET)
    GROUP_B.add(REVERSE_BULLET)
    m.MEDIA['reverse_shoot_sound'].play()
    
# Rainbow Multi-bullet
def MULTI_BULLET(GROUP_A, GROUP_B, POS):
    BULLET_1 = s.BULLET(POS, (6, 0), m.MEDIA['red_bullet'])
    BULLET_2 = s.BULLET(POS, (6, -6), m.MEDIA['orange_bullet'])
    BULLET_3 = s.BULLET(POS, (0, -6), m.MEDIA['yellow_bullet'])
    BULLET_4 = s.BULLET(POS, (-6, -6), m.MEDIA['green_bullet'])
    BULLET_5 = s.BULLET(POS, (-6, 0), m.MEDIA['blue_bullet'])
    BULLET_6 = s.BULLET(POS, (-6, 6), m.MEDIA['purple_bullet'])
    BULLET_7 = s.BULLET(POS, (0, 6), m.MEDIA['white_bullet'])
    BULLET_8 = s.BULLET(POS, (6, 6), m.MEDIA['grey_bullet'])
    groupa.add(BULLET_1, BULLET_2, BULLET_3, BULLET_4, BULLET_5, BULLET_6, BULLET_7, BULLET_8)
    groupb.add(BULLET_1, BULLET_2, BULLET_3, BULLET_4, BULLET_5, BULLET_6, BULLET_7, BULLET_8)
    m.MEDIA['multi_shoot_sound'].play()      

GAME_DICT = {
    # Player Media, Colors, And Locations
    'BLUE': {
        'COLOR': g.BLUE,
        'PLAYER_IMAGE': m.MEDIA['blue_face'],
        'BULLET_IMAGE': m.MEDIA['blue_bullet'],
        'LOCAL': 220,
        'ABILITY': BIG_BULLET},
    'ORANGE': {
        'COLOR': g.ORANGE,
        'PLAYER_IMAGE': m.MEDIA['orange_face'],
        'BULLET_IMAGE': m.MEDIA['orange_bullet'],
        'LOCAL': 220,
        'ABILITY': BIG_BULLET},
    'GREEN': {
        'COLOR': g.GREEN,
        'PLAYER_IMAGE': m.MEDIA['green_face'],
        'BULLET_IMAGE': m.MEDIA['green_bullet'],
        'LOCAL': 210,
        'ABILITY': SPLIT_BULLET,
        'SPLIT_BULLET_IMAGE': m.MEDIA['green_split_bullet']},
    'PURPLE': {
        'COLOR': g.PURPLE,
        'PLAYER_IMAGE': m.MEDIA['purple_face'],
        'BULLET_IMAGE': m.MEDIA['purple_bullet'],
        'LOCAL': 210,
        'ABILITY': LASER_BEAM},
    'RED': {
        'COLOR': g.RED,
        'PLAYER_IMAGE': m.MEDIA['red_face'],
        'BULLET_IMAGE': m.MEDIA['red_bullet'],
        'LOCAL': 224,
        'ABILITY': LASER_BEAM},
    'YELLOW': {
        'COLOR': g.YELLOW,
        'PLAYER_IMAGE': m.MEDIA['yellow_face'],
        'BULLET_IMAGE': m.MEDIA['yellow_bullet'],
        'LOCAL': 209,
        'ABILITY': SPLIT_BULLET,
        'SPLIT_BULLET_IMAGE': m.MEDIA['yellow_split_bullet']},
    'GREY': {
        'COLOR': g.GREY,
        'PLAYER_IMAGE': m.MEDIA['grey_face'],
        'BULLET_IMAGE': m.MEDIA['grey_bullet'],
        'LOCAL': 220,
        'ABILITY': REVERSE_BULLET},
    'WHITE': {
        'COLOR': g.WHITE,
        'PLAYER_IMAGE': m.MEDIA['white_face'],
        'BULLET_IMAGE': m.MEDIA['white_bullet'],
        'LOCAL': 210,
        'ABILITY': REVERSE_BULLET},
    'RAINBOW': {
        'COLOR': GET_RANDOM(),
        'PLAYER_IMAGE': m.MEDIA['rainbow_face'],
        'BULLET_IMAGE': m.MEDIA['rainbow_bullet'],
        'LOCAL': 190,
        'ABILITY': MULTI_BULLET},
    # HP Bars
    'HP': {
        0: m.MEDIA['hp_dead'],
        1: m.MEDIA['hp_low'],
        2: m.MEDIA['hp_decayed'],
        3: m.MEDIA['hp_full'],
        -1: m.MEDIA['hp_dead']},
    # Mode Values [Loaded In main game depending on g.MODE]
    'MODE': {
        'CLASSIC': {
            'TIMER': 30,
            'PLAYER_VELOCITY': 6,
            'BULLET_VELOCITY': 8,
            'HEALTH': 3,
            'SOUND': m.MEDIA['classic_sound'],
            'MUSIC': m.MEDIA['classic_music'],
            'DT': CLOCK.tick(60) / 1000},
        'CHAOS': {
            'TIMER': 10,
            'PLAYER_VELOCITY': 8,
            'BULLET_VELOCITY': 15,
            'HEALTH': 1,
            'SOUND': m.MEDIA['chaos_sound'], 
            'MUSIC': m.MEDIA['chaos_music'],
            'DT': CLOCK.tick(60) / 100}
        },
    # Timer Values
    'TIMER': {
        True: [g.RED, g.FONTB],
        False: [g.WHITE, g.FONTNORMAL]},
}     
