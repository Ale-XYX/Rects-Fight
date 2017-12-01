import pygame
import media32 as m32
import gamewide as Global

def Fetch(type1, type2, type3, insert1, insert2):
    if type1 == 'player':
        if type2 == 'player1':
            if type3 == 'image':
                if Global.P1Char == 1:
                    return m32.MEDIA[1]
                elif Global.P1Char == 2:
                    return m32.MEDIA[18]
                elif Global.P1Char == 3:
                    return m32.MEDIA[12]
                elif Global.P1Char == 4:
                    return m32.MEDIA[24]
                elif Global.P1Char == 5:
                    return m32.MEDIA[20]
                elif Global.P1Char == 6:
                    return m32.MEDIA[21]
                elif Global.P1Char == 7:
                    return m32.MEDIA[13]
                else:
                    return MEDIA[11]
            elif type3 == 'bullet':
                if Global.P1Char == 1:
                    return m32.MEDIA[2]
                elif Global.P1Char == 2:
                    return m32.MEDIA[5]
                elif Global.P1Char == 3:
                    return m32.MEDIA[3]
                elif Global.P1Char == 4:
                    return m32.MEDIA[8]
                elif Global.P1Char == 5:
                    return m32.MEDIA[6]
                elif Global.P1Char == 6:
                    return m32.MEDIA[7]
                elif Global.P1Char == 7:
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
                if Global.P2Char == 1:
                    return m32.MEDIA[1]
                elif Global.P2Char == 2:
                    return m32.MEDIA[18]
                elif Global.P2Char == 3:
                    return m32.MEDIA[12]
                elif Global.P2Char == 4:
                    return m32.MEDIA[24]
                elif Global.P2Char == 5:
                    return m32.MEDIA[20]
                elif Global.P2Char == 6:
                    return m32.MEDIA[21]
                elif Global.P2Char == 7:
                    return m32.MEDIA[13]
                else:
                    return MEDIA[11]
            elif type3 == 'bullet':
                if Global.P2Char == 1:
                    return m32.MEDIA[2]
                elif Global.P2Char == 2:
                    return m32.MEDIA[5]
                elif Global.P2Char == 3:
                    return m32.MEDIA[3]
                elif Global.P2Char == 4:
                    return m32.MEDIA[8]
                elif Global.P2Char == 5:
                    return m32.MEDIA[6]
                elif Global.P2Char == 6:
                    return m32.MEDIA[7]
                elif Global.P2Char == 7:
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
                if Global.P1Char == 1:
                    return Global.font.render('Blue', True, Global.blue)
                elif Global.P1Char == 2:
                    return Global.font.render('Orange', True, Global.orange)
                elif Global.P1Char == 3:
                    return Global.font.render('Green', True, Global.green)
                elif Global.P1Char == 4:
                    return Global.font.render('Yellow', True, Global.yellow)
                elif Global.P1Char == 5:
                    return Global.font.render('Purple', True, Global.purple)
                elif Global.P1Char == 6:
                    return Global.font.render('Red', True, Global.red)
                elif Global.P1Char == 7:
                    return Global.font.render('Grey', True, Global.grey)
                else:
                    return Global.font.render('NotFound', True, Global.white)
            elif type3 == 'player2':
                if Global.P2Char == 1:
                    return Global.font.render('Blue', True, Global.blue)
                elif Global.P2Char == 2:
                    return Global.font.render('Orange', True, Global.orange)
                elif Global.P2Char == 3:
                    return Global.font.render('Green', True, Global.green)
                elif Global.P2Char == 4:
                    return Global.font.render('Yellow', True, Global.yellow)
                elif Global.P2Char == 5:
                    return Global.font.render('Purple', True, Global.purple)
                elif Global.P2Char == 6:
                    return Global.font.render('Red', True, Global.red)
                elif Global.P2Char == 7:
                    return Global.font.render('Grey', True, Global.grey)
                else:
                    return Global.font.render('NotFound', True, Global.white)
            else:
                return Global.font.render('NotFound', True, Global.white)
        elif type2 == 'playerColor':
            if insert1.health == 0:
                if Global.P1Char == 1:
                    return Global.blue
                elif Global.P1Char == 2:
                    return Global.orange
                elif Global.P1Char == 3:
                    return Global.green
                elif Global.P1Char == 4:
                    return Global.yellow
                elif Global.P1Char == 5:
                    return Global.purple
                elif Global.P1Char == 6:
                    return Global.red
                elif Global.P1Char == 7:
                    return Global.grey
                else:
                    return Global.white
            elif insert2.health == 0:
                if Global.P2Char == 1:
                    return Global.blue
                elif Global.P2Char == 2:
                    return Global.orange
                elif Global.P2Char == 3:
                    return Global.green
                elif Global.P2Char == 4:
                    return Global.yellow
                elif Global.P2Char == 5:
                    return Global.purple
                elif Global.P2Char == 6:
                    return Global.red
                elif Global.P2Char == 7:
                    return Global.grey
                else:
                    return Global.white
            else:
                return Global.white
        elif type2 == 'timer':
            if insert1 < 10:
                return Global.red
            else:
                return Global.white
        else:
            print('Fetch() has encountered an error, Aborting Game')
            sys.exit()
