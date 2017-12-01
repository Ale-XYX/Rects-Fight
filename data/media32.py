
# Media Names:
# ------------
# 1: Blue Player
# 2: Blue Bullet
# 3: Green Bullet
# 4: Grey Bullet
# 5: Orange Bullet
# 6: Purple Bullet
# 7: Red Bullet
# 8: Yellow Bullet
# 9: Dead HP Bar
# 10: EGG
# 11: Error Image
# 12: Green Player
# 13: Grey Player
# 14: Full HP Bar
# 15: Damaged HP Bar
# 16: Low HP Bar
# 17: Game Icon
# 18: Orange Player
# 19: Pause Screen
# 20: Purple Player
# 21: Red Player
# 22: Title Screen
# 23: Wall
# 24: Yellow Player
# ----- Audio -----
# 25: Die Sound
# 26: Fight Sound
# 27: Hit Sound
# 28: Music
# 29: Pause Sound
# 30: Select Sound
# 31: Shoot Sound
# 32: Start Sound
             
import pygame
import os
import glob

pygame.init()

screen = pygame.display.set_mode((500, 600))
namer = 0
MEDIA = {}
files = glob.glob(os.path.join(os.path.dirname(__file__), 'media', 'image', '*.png'))
files2 = glob.glob(os.path.join(os.path.dirname(__file__), 'media', 'audio', '*.wav'))

for file_name in files:
    obj = pygame.image.load(file_name).convert_alpha()
    namer += 1
    MEDIA[namer] = obj
        
for file_name in files2:
    obj = pygame.mixer.Sound(file_name)
    namer += 1
    MEDIA[namer] = obj
        
pygame.display.set_caption('Rects Fight!')
pygame.display.set_icon(MEDIA[17])
