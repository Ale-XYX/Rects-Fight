import media as m
import var as v
import datetime
import random

def get_rainbow_random():
    i = random.randrange(0, 6)
    if i == 0:
        return v.blue
    if i == 1:
        return v.orange
    if i == 2:
        return v.green
    if i == 3:
        return v.purple
    if i == 4:
        return v.red
    if i == 5:
        return v.yellow
    if i == 6:
        return v.white
GAME_MEDIA = {
    'Blue': {
        'color': v.blue,
        'player_image': m.MEDIA['blue'],
        'bullet_image': m.MEDIA['bulletblue'],
        'local': 220},
    'Orange': {
        'color': v.orange,
        'player_image': m.MEDIA['orange'],
        'bullet_image': m.MEDIA['bulletorange'],
        'local': 200},
    'Green': {
        'color': v.green,
        'player_image': m.MEDIA['green'],
        'bullet_image': m.MEDIA['bulletgreen'],
        'local': 210},
    'Purple': {
        'color': v.purple,
        'player_image': m.MEDIA['purple'],
        'bullet_image': m.MEDIA['bulletpurple'],
        'local': 210},
    'Red': {
        'color': v.red,
        'player_image': m.MEDIA['red'],
        'bullet_image': m.MEDIA['bulletred'],
        'local': 224},
    'Yellow': {
        'color': v.yellow,
        'player_image': m.MEDIA['yellow'],
        'bullet_image': m.MEDIA['bulletyellow'],
        'local': 209},
    'Grey': {
        'color': v.grey,
        'player_image': m.MEDIA['grey'],
        'bullet_image': m.MEDIA['bulletgrey'],
        'local': 220},
    'White': {
        'color': v.white,
        'player_image': m.MEDIA['white'],
        'bullet_image': m.MEDIA['bulletgrey'],
        'local': 200},
    'Rainbow': {
        'color': get_rainbow_random(),
        'player_image': m.MEDIA['rainbow'],
        'bullet_image': m.MEDIA['bulletrainbow'],
        'local': 200},
    'HP': {
        0: m.MEDIA['dead'],
        1: m.MEDIA['hp3'],
        2: m.MEDIA['hp2'],
        3: m.MEDIA['hp1']},
}


print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'DICT: ' + 'Loaded Game Media Dictionary')
