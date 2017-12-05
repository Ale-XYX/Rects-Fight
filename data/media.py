import pygame
import os
import glob
import datetime
import var as v

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 600))
MEDIA = {}
files = glob.glob(os.path.join(os.path.dirname(__file__), 'media', 'image', '*.png'))
files2 = glob.glob(os.path.join(os.path.dirname(__file__), 'media', 'audio', '*.wav'))

for file_name in files:
    obj = pygame.image.load(file_name).convert_alpha()
    MEDIA[os.path.split(file_name)[-1][:-4]] = obj
    
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'MEDIA: ' + 'Loaded Images')

for file_name in files2:
    obj = pygame.mixer.Sound(file_name)
    MEDIA[os.path.split(file_name)[-1][:-4]] = obj
    
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'MEDIA: ' + 'Loaded Audio')

pygame.display.set_caption('Rects Fight!')
pygame.display.set_icon(MEDIA['icon'])
