import pygame
import media as Media
import gamewide as Global
def Fetch(type1, type2, type3, insert1, insert2):
    if type1 == 'player':
        if type2 == 'player1':
            if type3 == 'image':
                if Global.P1Char == 1:
                    return Media.blue
                elif Global.P1Char == 2:
                    return Media.orange
                elif Global.P1Char == 3:
                    return Media.green
                elif Global.P1Char == 4:
                    return Media.yellow
                elif Global.P1Char == 5:
                    return Media.purple
                elif Global.P1Char == 6:
                    return Media.red
                elif Global.P1Char == 7:
                    return Media.grey
                else:
                    return Media.error
            elif type3 == 'bullet':
                if Global.P1Char == 1:
                    return Media.bulletblue
                elif Global.P1Char == 2:
                    return Media.bulletorange
                elif Global.P1Char == 3:
                    return Media.bulletgreen
                elif Global.P1Char == 4:
                    return Media.bulletyellow
                elif Global.P1Char == 5:
                    return Media.bulletpurple
                elif Global.P1Char == 6:
                    return Media.bulletred
                elif Global.P1Char == 7:
                    return Media.bulletgrey
                else:
                    return Media.error
            elif type3 == 'hp':
                if insert1.health == 3:
                    return pygame.transform.flip(Media.hp1, True, False)
                elif insert1.health == 2:
                    return pygame.transform.flip(Media.hp2, True, False)
                elif insert1.health == 1:
                    return pygame.transform.flip(Media.hp3, True, False)
                elif insert1.health <= 0:
                    return pygame.transform.flip(Media.dead, True, False)
                else:
                    return Media.error
            else:
                return Media.error
        elif type2 == 'player2':
            if type3 == 'image':
                if Global.P2Char == 1:
                    return Media.blue
                elif Global.P2Char == 2:
                    return Media.orange
                elif Global.P2Char == 3:
                    return Media.green
                elif Global.P2Char == 4:
                    return Media.yellow
                elif Global.P2Char == 5:
                    return Media.purple
                elif Global.P2Char == 6:
                    return Media.red
                elif Global.P2Char == 7:
                    return Media.grey
                else:
                    return Media.error
            elif type3 == 'bullet':
                if Global.P2Char == 1:
                    return Media.bulletblue
                elif Global.P2Char == 2:
                    return Media.bulletorange
                elif Global.P2Char == 3:
                    return Media.bulletgreen
                elif Global.P2Char == 4:
                    return Media.bulletyellow
                elif Global.P2Char == 5:
                    return Media.bulletpurple
                elif Global.P2Char == 6:
                    return Media.bulletred
                elif Global.P2char == 7:
                    return Media.bulletgrey
                else:
                    return Media.error
            elif type3 == 'hp':
                if insert2.health == 3:
                    return Media.hp1
                if insert2.health == 2:
                    return Media.hp2
                if insert2.health == 1:
                    return Media.hp3
                if insert2.health <= 0:
                    return Media.dead
                else:
                    return Media.error
            else:
                return Media.error
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
