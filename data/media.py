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

PLAYER_MEDIA = {
    'Blue': {
        'color': v.blue,
        'player_image': MEDIA['blue'],
        'bullet_image': MEDIA['bulletblue'],
        'local': 0},
    'Orange': {
        'color': v.orange,
        'player_image': MEDIA['orange'],
        'bullet_image': MEDIA['bulletorange'],
        'local': 55},
    'Green': {
        'color': v.green,
        'player_image': MEDIA['green'],
        'bullet_image': MEDIA['bulletgreen'],
        'local': 110},
    'Purple': {
        'color': v.purple,
        'player_image': MEDIA['purple'],
        'bullet_image': MEDIA['bulletpurple'],
        'local': 165},
    'Red': {
        'color': v.red,
        'player_image': MEDIA['red'],
        'bullet_image': MEDIA['bulletred'],
        'local': 220},
    'Yellow': {
        'color': v.yellow,
        'player_image': MEDIA['yellow'],
        'bullet_image': MEDIA['bulletyellow'],
        'local': 275},
    'Grey': {
        'color': v.grey,
        'player_image': MEDIA['grey'],
        'bullet_image': MEDIA['bulletgrey'],
        'local': 330}
    }

print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'MEDIA: ' + 'Loaded Player Media Dictionary')

