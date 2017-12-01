import pygame
import media32 as m32
import var as v

def Fetch(type1, type2, type3, insert1, insert2):
    if type1 == 'player':
        if type2 == 'player1':
            if type3 == 'image':
                if v.P1Char == 1:
                    return m32.MEDIA[1]
                elif v.P1Char == 2:
                    return m32.MEDIA[18]
                elif v.P1Char == 3:
                    return m32.MEDIA[12]
                elif v.P1Char == 4:
                    return m32.MEDIA[24]
                elif v.P1Char == 5:
                    return m32.MEDIA[20]
                elif v.P1Char == 6:
                    return m32.MEDIA[21]
                elif v.P1Char == 7:
                    return m32.MEDIA[13]
                else:
                    return MEDIA[11]
            elif type3 == 'bullet':
                if v.P1Char == 1:
                    return m32.MEDIA[2]
                elif v.P1Char == 2:
                    return m32.MEDIA[5]
                elif v.P1Char == 3:
                    return m32.MEDIA[3]
                elif v.P1Char == 4:
                    return m32.MEDIA[8]
                elif v.P1Char == 5:
                    return m32.MEDIA[6]
                elif v.P1Char == 6:
                    return m32.MEDIA[7]
                elif v.P1Char == 7:
                    return m32.MEDIA[4]
                else:
                    return m32.MEDIA[11]
            elif type3 == 'hp':
                if insert1.health == 3:
                    return pygame.transform.flip(m32.MEDIA[14], True, False)
                elif insert1.health == 2:
                    return pygame.transform.flip(m32.MEDIA[15], True, False)
                elif insert1.health == 1:
                    return pygame.transform.flip(m32.MEDIA[16], True, False)
                elif insert1.health <= 0:
                    return pygame.transform.flip(m32.MEDIA[9], True, False)
                else:
                    return Media.error
            else:
                return Media.error
        elif type2 == 'player2':
            if type3 == 'image':
                if v.P2Char == 1:
                    return m32.MEDIA[1]
                elif v.P2Char == 2:
                    return m32.MEDIA[18]
                elif v.P2Char == 3:
                    return m32.MEDIA[12]
                elif v.P2Char == 4:
                    return m32.MEDIA[24]
                elif v.P2Char == 5:
                    return m32.MEDIA[20]
                elif v.P2Char == 6:
                    return m32.MEDIA[21]
                elif v.P2Char == 7:
                    return m32.MEDIA[13]
                else:
                    return MEDIA[11]
            elif type3 == 'bullet':
                if v.P2Char == 1:
                    return m32.MEDIA[2]
                elif v.P2Char == 2:
                    return m32.MEDIA[5]
                elif v.P2Char == 3:
                    return m32.MEDIA[3]
                elif v.P2Char == 4:
                    return m32.MEDIA[8]
                elif v.P2Char == 5:
                    return m32.MEDIA[6]
                elif v.P2Char == 6:
                    return m32.MEDIA[7]
                elif v.P2Char == 7:
                    return m32.MEDIA[4]
                else:
                    return MEDIA[11]
            elif type3 == 'hp':
                if insert2.health == 3:
                    return m32.MEDIA[14]
                if insert2.health == 2:
                    return m32.MEDIA[15]
                if insert2.health == 1:
                    return m32.MEDIA[16]
                if insert2.health <= 0:
                    return m32.MEDIA[9]
                else:
                    return m32.MEDIA[11]
            else:
                return m32.MEDIA[11]
    elif type1 == 'text':
        if type2 == 'player':
            if type3 == 'player1':
                if v.P1Char == 1:
                    return v.font.render('Blue', True, v.blue)
                elif v.P1Char == 2:
                    return v.font.render('Orange', True, v.orange)
                elif v.P1Char == 3:
                    return v.font.render('Green', True, v.green)
                elif v.P1Char == 4:
                    return v.font.render('Yellow', True, v.yellow)
                elif v.P1Char == 5:
                    return v.font.render('Purple', True, v.purple)
                elif v.P1Char == 6:
                    return v.font.render('Red', True, v.red)
                elif v.P1Char == 7:
                    return v.font.render('Grey', True, v.grey)
                else:
                    return v.font.render('NotFound', True, v.white)
            elif type3 == 'player2':
                if v.P2Char == 1:
                    return v.font.render('Blue', True, v.blue)
                elif v.P2Char == 2:
                    return v.font.render('Orange', True, v.orange)
                elif v.P2Char == 3:
                    return v.font.render('Green', True, v.green)
                elif v.P2Char == 4:
                    return v.font.render('Yellow', True, v.yellow)
                elif v.P2Char == 5:
                    return v.font.render('Purple', True, v.purple)
                elif v.P2Char == 6:
                    return v.font.render('Red', True, v.red)
                elif v.P2Char == 7:
                    return v.font.render('Grey', True, v.grey)
                else:
                    return v.font.render('NotFound', True, v.white)
            else:
                return v.font.render('NotFound', True, v.white)
        elif type2 == 'playerColor':
            if insert1.health == 0:
                if v.P1Char == 1:
                    return v.blue
                elif v.P1Char == 2:
                    return v.orange
                elif v.P1Char == 3:
                    return v.green
                elif v.P1Char == 4:
                    return v.yellow
                elif v.P1Char == 5:
                    return v.purple
                elif v.P1Char == 6:
                    return v.red
                elif v.P1Char == 7:
                    return v.grey
                else:
                    return v.white
            elif insert2.health == 0:
                if v.P2Char == 1:
                    return v.blue
                elif v.P2Char == 2:
                    return v.orange
                elif v.P2Char == 3:
                    return v.green
                elif v.P2Char == 4:
                    return v.yellow
                elif v.P2Char == 5:
                    return v.purple
                elif v.P2Char == 6:
                    return v.red
                elif v.P2Char == 7:
                    return v.grey
                else:
                    return v.white
            else:
                return v.white
        elif type2 == 'timer':
            if insert1 < 10:
                return v.red
            else:
                return v.white
        else:
            print('Fetch() has encountered an error, Aborting Game')
            sys.exit()
