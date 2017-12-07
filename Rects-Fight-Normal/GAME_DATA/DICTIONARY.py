# DICTIONARY
import MEDIA as m
import GLOBAL as g
import random

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
        
GAME_DICT = {
    # Player Media, Colors, And Locations
    'BLUE': {
        'COLOR': g.BLUE,
        'PLAYER_IMAGE': m.MEDIA['blue_face'],
        'BULLET_IMAGE': m.MEDIA['blue_bullet'],
        'LOCAL': 220},
    'ORANGE': {
        'COLOR': g.ORANGE,
        'PLAYER_IMAGE': m.MEDIA['orange_face'],
        'BULLET_IMAGE': m.MEDIA['orange_bullet'],
        'LOCAL': 200},
    'GREEN': {
        'COLOR': g.GREEN,
        'PLAYER_IMAGE': m.MEDIA['green_face'],
        'BULLET_IMAGE': m.MEDIA['green_bullet'],
        'LOCAL': 210},
    'PURPLE': {
        'COLOR': g.PURPLE,
        'PLAYER_IMAGE': m.MEDIA['purple_face'],
        'BULLET_IMAGE': m.MEDIA['purple_bullet'],
        'LOCAL': 210},
    'RED': {
        'COLOR': g.RED,
        'PLAYER_IMAGE': m.MEDIA['red_face'],
        'BULLET_IMAGE': m.MEDIA['red_bullet'],
        'LOCAL': 224},
    'YELLOW': {
        'COLOR': g.YELLOW,
        'PLAYER_IMAGE': m.MEDIA['yellow_face'],
        'BULLET_IMAGE': m.MEDIA['yellow_bullet'],
        'LOCAL': 209},
    'GREY': {
        'COLOR': g.GREY,
        'PLAYER_IMAGE': m.MEDIA['grey_face'],
        'BULLET_IMAGE': m.MEDIA['grey_bullet'],
        'LOCAL': 220},
    'WHITE': {
        'COLOR': g.WHITE,
        'PLAYER_IMAGE': m.MEDIA['white_face'],
        'BULLET_IMAGE': m.MEDIA['white_bullet'],
        'LOCAL': 210},
    'RAINBOW': {
        'COLOR': GET_RANDOM(),
        'PLAYER_IMAGE': m.MEDIA['rainbow_face'],
        'BULLET_IMAGE': m.MEDIA['rainbow_bullet'],
        'LOCAL': 190},
    # HP Bars
    'HP': {
        0: m.MEDIA['hp_dead'],
        1: m.MEDIA['hp_low'],
        2: m.MEDIA['hp_decayed'],
        3: m.MEDIA['hp_full']},
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
