import pygame
import os
import glob
import datetime
import var as v
logat = str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'MEDIA: '

pygame.init()

screen = pygame.display.set_mode((500, 600))
namer = 0
MEDIA = {}
files = glob.glob(os.path.join(os.path.dirname(__file__), 'media', 'image', '*.png'))
files2 = glob.glob(os.path.join(os.path.dirname(__file__), 'media', 'audio', '*.wav'))

for file_name in files:
    obj = pygame.image.load(file_name).convert_alpha()
    MEDIA[os.path.split(file_name)[-1][:-4]] = obj
    
print(logat + 'Loaded Images')

for file_name in files2:
    obj = pygame.mixer.Sound(file_name)
    namer += 1
    MEDIA[os.path.split(file_name)[-1][:-4]] = obj
    
print(logat + 'Loaded Audio')

pygame.display.set_caption('Rects Fight!')
pygame.display.set_icon(MEDIA['icon'])

PLAYER_MEDIA = {
    'Blue': {
        'color': v.blue,
        'player_image': MEDIA['blue'],
        'bullet_image': MEDIA['bulletblue']},
    'Orange': {
        'color': v.orange,
        'player_image': MEDIA['orange'],
        'bullet_image': MEDIA['bulletorange']},
    'Green': {
        'color': v.green,
        'player_image': MEDIA['green'],
        'bullet_image': MEDIA['bulletgreen']},
    'Purple': {
        'color': v.purple,
        'player_image': MEDIA['purple'],
        'bullet_image': MEDIA['bulletpurple']},
    'Red': {
        'color': v.red,
        'player_image': MEDIA['red'],
        'bullet_image': MEDIA['bulletred']},
    'Yellow': {
        'color': v.yellow,
        'player_image': MEDIA['yellow'],
        'bullet_image': MEDIA['bulletyellow']},
    'Grey': {
        'color': v.grey,
        'player_image': MEDIA['grey'],
        'bullet_image': MEDIA['bulletgrey']}
    }

print(logat + 'Loaded Player Media Dictionary')

