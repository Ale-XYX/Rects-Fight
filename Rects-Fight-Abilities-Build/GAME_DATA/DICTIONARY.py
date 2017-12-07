# DICTIONARY
import MEDIA as m
import GLOBAL as g
import SPRITES as s
import random
import pygame

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
def BIG_BULLET(groupa, groupb, pos, vel, img):
    if not vel[0] == 0:
        if not vel[0] == -8:
            vel = (vel[0] - 4, 0)
        else:
            vel = (vel[0] + 4, 0)
    if not vel[1] == 0 and vel[0] == 0:
        if not vel[1] == -8:
            vel = (0, vel[1] - 4)
        else:
            vel = (0, vel[1] + 4)
    BIGBULLET = s.BigBullet(pos, vel, img)
    groupa.add(BIGBULLET)
    groupb.add(BIGBULLET)
    m.MEDIA['big_shoot_sound'].play()
    
# Rainbow Multi-bullet
def MULTI_BULLET(groupa, groupb, pos):
    BULLET1 = s.Bullet(pos, (6, 0), m.MEDIA['red_bullet'])
    BULLET2 = s.Bullet(pos, (6, -6), m.MEDIA['orange_bullet'])
    BULLET3 = s.Bullet(pos, (0, -6), m.MEDIA['yellow_bullet'])
    BULLET4 = s.Bullet(pos, (-6, -6), m.MEDIA['green_bullet'])
    BULLET5 = s.Bullet(pos, (-6, 0), m.MEDIA['blue_bullet'])
    BULLET6 = s.Bullet(pos, (-6, 6), m.MEDIA['purple_bullet'])
    BULLET7 = s.Bullet(pos, (0, 6), m.MEDIA['white_bullet'])
    BULLET8 = s.Bullet(pos, (6, 6), m.MEDIA['grey_bullet'])
    groupa.add(BULLET1, BULLET2, BULLET3, BULLET4, BULLET5, BULLET6, BULLET7, BULLET8)
    groupb.add(BULLET1, BULLET2, BULLET3, BULLET4, BULLET5, BULLET6, BULLET7, BULLET8)
    m.MEDIA['multi_shoot_sound'].play()

def PURPLE_LASER_BEAM(groupa, groupb, pos, vel):
    if vel[0] == 8 and vel[1] == 0:
        vel = (vel[0] - 3, vel[1])
    elif vel[0] == -8 and vel[1] == 0:
        vel = (vel[0] + 3, vel[1])
    elif vel[0] == 0 and vel[1] == 8:
        vel = (vel[0], vel[1] - 3)
    elif vel[0] == 0 and vel[1] == -8:
        vel = (vel[0], vel[1] + 3)
    BEAM = s.PurpleBeam(pos, vel)
    groupa.add(BEAM)
    groupb.add(BEAM)

def RED_LASER_BEAM(groupa, groupb, pos, vel):
    if vel[0] == 8 and vel[1] == 0:
        vel = (vel[0] - 3, vel[1])
    elif vel[0] == -8 and vel[1] == 0:
        vel = (vel[0] + 3, vel[1])
    elif vel[0] == 0 and vel[1] == 8:
        vel = (vel[0], vel[1] - 3)
    elif vel[0] == 0 and vel[1] == -8:
        vel = (vel[0], vel[1] + 3)
    BEAM = s.RedBeam(pos, vel)
    groupa.add(BEAM)
    groupb.add(BEAM)
    
def SPLIT_BULLET(groupa, groupb, pos, vel, img, color):
    SPLIT_BULLET = s.SplitBullet(pos, vel, img, groupa, groupb, color)
    groupa.add(SPLIT_BULLET)
    groupb.add(SPLIT_BULLET)
    
def TEMP_DEFAULT(groupa, groupb, pos, vel, img):
    BULLET = s.Bullet(pos, vel, img)
    groupa.add(BULLET)
    groupb.add(BULLET)
    m.MEDIA['shoot_sound'].play()
        
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
        'ABILITY': PURPLE_LASER_BEAM},
    'RED': {
        'COLOR': g.RED,
        'PLAYER_IMAGE': m.MEDIA['red_face'],
        'BULLET_IMAGE': m.MEDIA['red_bullet'],
        'LOCAL': 224,
        'ABILITY': RED_LASER_BEAM},
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
        'ABILITY': TEMP_DEFAULT},
    'WHITE': {
        'COLOR': g.WHITE,
        'PLAYER_IMAGE': m.MEDIA['white_face'],
        'BULLET_IMAGE': m.MEDIA['white_bullet'],
        'LOCAL': 210,
        'ABILITY': TEMP_DEFAULT},
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
            'PLAYER_VELOCITY': 5,
            'BULLET_VELOCITY': 8,
            'HEALTH': 3,
            'SOUND': m.MEDIA['classic_sound'],
            'MUSIC': m.MEDIA['classic_music']},
        'CHAOS': {
            'TIMER': 10,
            'PLAYER_VELOCITY': 8,
            'BULLET_VELOCITY': 15,
            'HEALTH': 1,
            'SOUND': m.MEDIA['chaos_sound'], 
            'MUSIC': m.MEDIA['chaos_music']}
        },
    # Timer Values
    'TIMER': {
        True: [g.RED, g.FONTB],
        False: [g.WHITE, g.FONTNORMAL]},
}     
