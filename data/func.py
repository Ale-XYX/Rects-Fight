import pygame
import datetime
import media as m
import var as v

pygame.init()

def get(type1, insert):
    if type1 == 'char':
        image = m.PLAYER_MEDIA[insert]['player_image']
        color = m.PLAYER_MEDIA[insert]['color']
        text = v.font.render(insert, True, color)
        return image, text
    elif type1 == 'hp1':
        if insert.health == 3:
            return pygame.transform.flip(m.MEDIA['hp1'], True, False)
        elif insert.health == 2:
            return pygame.transform.flip(m.MEDIA['hp2'], True, False)
        elif insert.health == 1:
            return pygame.transform.flip(m.MEDIA['hp3'], True, False)
        elif insert.health == 0:
            return pygame.transform.flip(m.MEDIA['dead'], True, False)
    elif type1 == 'hp2':
        if insert.health == 3:
            return m.MEDIA['hp1']
        elif insert.health == 2:
            return m.MEDIA['hp2']
        elif insert.health == 1:
            return m.MEDIA['hp3']
        elif insert.health == 0:
            return m.MEDIA['dead']
    elif type1 == 'time':
        if insert <= 10:
            return v.font4.render(str(round(insert, 1)), True, v.red)
        else:
            return v.font.render(str(round(insert, 1)), True, v.white)
    elif type1 == 'local':
        if insert == 0:
            return 220
        elif insert == 1:
            return 200
        elif insert == 2:
            return 210
        elif insert == 3:
            return 210
        elif insert == 4:
            return 224
        elif insert == 5:
            return 209
        elif insert == 6:
            return 220
    
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'FUNC: ' + 'Loaded Get()')
        
