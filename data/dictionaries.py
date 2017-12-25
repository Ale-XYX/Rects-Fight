import globals
import pygame
import random
import os
import glob

pygame.init()

# Media Dictionary
# Loads sounds/images into dictionary based on filename
MEDIA = {}
image_files = glob.glob(os.path.join(os.path.dirname(__file__), 'media_files', 'image_files', '*.png'))
audio_files = glob.glob(os.path.join(os.path.dirname(__file__), 'media_files', 'audio_files', '*.wav'))

for file in image_files:
    obj = pygame.image.load(file).convert_alpha()
    MEDIA[os.path.split(file)[-1][:-4]] = obj

for file in audio_files:
    obj = pygame.mixer.Sound(file)
    MEDIA[os.path.split(file)[-1][:-4]] = obj

PLAYER_MEDIA = {
    'Blue': {
        'Color': globals.BLUE,
        'Image': MEDIA['blue_face'],
        'Bullet_Image': MEDIA['blue_bullet'],
        'Location': (220, 145),
        'Parameters': [MEDIA['blue_big_bullet'], 'Big_Bullet']
    },
    'Orange': {
        'Color': globals.ORANGE,
        'Image': MEDIA['orange_face'],
        'Bullet_Image': MEDIA['orange_bullet'],
        'Location': (208, 145),
        'Parameters': [MEDIA['orange_big_bullet'], 'Big_Bullet']
    },
    'Green': {
        'Color': globals.GREEN,
        'Image': MEDIA['green_face'],
        'Bullet_Image': MEDIA['green_bullet'],
        'Split_Bullet_Image': MEDIA['green_split_bullet'],
        'Location': (210, 135),
        'Parameters': [MEDIA['green_split_bullet'], 'Green']
    },
    'Yellow': {
        'Color': globals.YELLOW,
        'Image': MEDIA['yellow_face'],
        'Bullet_Image': MEDIA['yellow_bullet'],
        'Split_Bullet_Image': MEDIA['yellow_split_bullet'],
        'Location': (209, 135),
        'Parameters': [MEDIA['yellow_split_bullet'], 'Yellow']
    },
    'Red': {
        'Color': globals.RED,
        'Image': MEDIA['red_face'],
        'Bullet_Image': MEDIA['red_bullet'],
        'Location': (224, 160),
        'Parameters': ['Red']
    },
    'Purple': {
        'Color': globals.PURPLE,
        'Image': MEDIA['purple_face'],
        'Bullet_Image': MEDIA['purple_bullet'],
        'Location': (211, 160),
        'Parameters': ['Purple']
    },
    'Grey': {
        'Color': globals.GREY,
        'Image': MEDIA['grey_face'],
        'Bullet_Image': MEDIA['grey_bullet'],
        'Location': (220, 115),
        'Parameters': [MEDIA['grey_boomerang_bullet'], 'Grey']
    },
    'White': {
        'Color': globals.WHITE,
        'Image': MEDIA['white_face'],
        'Bullet_Image': MEDIA['white_bullet'],
        'Location': (210, 115),
        'Parameters': [MEDIA['white_boomerang_bullet'], 'White']
    },
    'Rainbow': {
        'Color': random.choice((
            globals.RED, globals.ORANGE, globals.YELLOW, globals.GREEN, globals.BLUE, globals.PURPLE
        )),
        'Image': MEDIA['rainbow_face'],
        'Bullet_Image': MEDIA['rainbow_bullet'],
        'Location': (200, 135),
    }
}

VELOCITY_VALUES = {
    'Convert': {
        'Big_Bullet': {
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
            (0, -16): (0, -8),
        },
        'Laser': {
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
            (0, -16): lambda bullet: -(bullet.vel[1] - 20)
        },
        'Split_Bullet': {
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
            (0, -16): [(0, 16), (10, 16), (-10, 16)]
        },
        'Reverse_Bullet': {
            'Velocity': {
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
                (0, -16): (0, -12)
            },
            'Direction': {
                (8, 0): 'Right',
                (-8, 0): 'Left',
                (0, 8): 'Down',
                (0, -8): 'Up',
                (10, 0): 'Medium_Right',
                (-10, 0): 'Medium_Left',
                (0, 10): 'Medium_Down',
                (0, -10): 'Medium_Up',
                (12, 0): 'Fast_Right',
                (-12, 0): 'Fast_Left',
                (0, 12): 'Fast_Down',
                (0, -12): 'Fast_Up'
            },
            'White': {
                'Right': lambda self: (self.vel[0] - 0.2, self.vel[1] + 0.02),
                'Left': lambda self: (self.vel[0] + 0.2, self.vel[1] + 0.02),
                'Up': lambda self: (self.vel[0] - 0.02, self.vel[1] + 0.2),
                'Down': lambda self: (self.vel[0] -   0.02, self.vel[1] - 0.2),

                'Medium_Right': lambda self: (self.vel[0] - 0.4, self.vel[1] + 0.1),
                'Medium_Left': lambda self: (self.vel[0] + 0.4, self.vel[1] + 0.1),
                'Medium_Up': lambda self: (self.vel[0] - 0.1, self.vel[1] + 0.4),
                'Medium_Down': lambda self: (self.vel[0] - 0.1, self.vel[1] - 0.4),

                'Fast_Right': lambda self: (self.vel[0] - 0.6, self.vel[1] + 0.2),
                'Fast_Left': lambda self: (self.vel[0] + 0.6, self.vel[1] + 0.2),
                'Fast_Up': lambda self: (self.vel[0] - 0.2, self.vel[1] + 0.6),
                'Fast_Down': lambda self: (self.vel[0] - 0.2, self.vel[1] - 0.6)},
            'Grey': {
                'Right': lambda self: (self.vel[0] - 0.2, self.vel[1] - 0.02),
                'Left': lambda self: (self.vel[0] + 0.2, self.vel[1] - 0.02),
                'Up': lambda self: (self.vel[0] + 0.02, self.vel[1] + 0.2),
                'Down': lambda self: (self.vel[0] + 0.02, self.vel[1] - 0.2),

                'Medium_Right': lambda self: (self.vel[0] - 0.4, self.vel[1] - 0.1),
                'Medium_Left': lambda self: (self.vel[0] + 0.4, self.vel[1] - 0.1),
                'Medium_Up': lambda self: (self.vel[0] + 0.1, self.vel[1] + 0.4),
                'Medium_Down': lambda self: (self.vel[0] + 0.1, self.vel[1] - 0.4),

                'Fast_Right': lambda self: (self.vel[0] - 0.6, self.vel[1] - 0.2),
                'Fast_Left': lambda self: (self.vel[0] + 0.6, self.vel[1] - 0.2),
                'Fast_Up': lambda self: (self.vel[0] + 0.2, self.vel[1] + 0.6),
                'Fast_Down': lambda self: (self.vel[0] + 0.2, self.vel[1] - 0.6)
                }
        },
        'Multi_Bullet': {
            'Classic': {
                1: (5, 0),
                2: (5, -5),
                3: (0, -5),
                4: (-5, -5),
                5: (-5, 0),
                6: (-5, 5),
                7: (0, 5),
                8: (5, 5)
            },
            'Tense': {
                1: (7, 0),
                2: (7, -7),
                3: (0, -7),
                4: (-7, -7),
                5: (-7, 0),
                6: (-7, 7),
                7: (0, 7),
                8: (7, 7)
            },
            'Chaos': {
                1: (9, 0),
                2: (9, -9),
                3: (0, -9),
                4: (-9, -9),
                5: (-9, 0),
                6: (-9, 9),
                7: (0, 9),
                8: (9, 9)
                }
        }
    },
    'Compare': {
        'Laser_Image': {
            'Purple': {
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
                (0, -16): pygame.transform.rotate(MEDIA['purple_laser'], 90)
            },
            'Red': {
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
                (0, -16): pygame.transform.rotate(MEDIA['red_laser'], 90)
                    }
                }
            }
        }



MODE_VALUES = {
    'Classic': {
        'Timer': 30,
        'Player_Velocity': 6,
        'Bullet_Velocity': 8,
        'Health': 3,
        'Sound': MEDIA['classic_sound'],
        'Music': MEDIA['classic_music'],
        'Cooldown': 3,
        'Color': globals.GREEN,
        'Location': (220, 190)
    },
    'Tense': {
        'Timer': 20,
        'Player_Velocity': 7,
        'Bullet_Velocity': 12,
        'Health': 2,
        'Sound': MEDIA['tense_sound'],
        'Music': MEDIA['tense_music'],
        'Cooldown': 1,
        'Color': globals.YELLOW,
        'Location': (220, 290)
    },
    'Chaos': {
        'Timer': 10,
        'Player_Velocity': 8,
        'Bullet_Velocity': 16,
        'Health': 1,
        'Sound': MEDIA['chaos_sound'],
        'Music': MEDIA['chaos_music'],
        'Cooldown': 0.3,
        'Color': globals.RED,
        'Location': (220, 390)
    }
}

# HP Bars
# Using player.health, return images
HP_MEDIA = {
    0: MEDIA['hp_dead'],
    1: MEDIA['hp_low'],
    2: MEDIA['hp_decayed'],
    3: MEDIA['hp_full'],
    -1: MEDIA['hp_dead']
}
# Timer Values
# Using a comparison timer, return a font
TIMER_DICT = {
    True: [globals.RED, globals.FONT_BOLD],
    False: [globals.WHITE, globals.FONT_BIG]
    }