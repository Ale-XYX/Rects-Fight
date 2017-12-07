# MEDIA
import pygame
import os
import glob

pygame.init()
pygame.mixer.init()

# Setting Up Items
SCREEN = pygame.display.set_mode((500, 600))
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
