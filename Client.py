if __name__ == '__main__':
    import pygame
    import sys
    import datetime
    
    print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'CLIENT: ' + 'Loading Rects Fight V1.6')
    sys.path.insert(0, './data')
    import game as g
    import var as v
    print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'CLIENT: ' + 'Load Complete')
    pygame.init()
    print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'CLIENT: ' + 'Game Init')
    g.title()
    g.char_select()
    print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'CLIENT: ' + 'Main init')
    while v.superloop:
        g.main()
    print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'CLIENT: ' + 'Game ended, closing')
    pygame.quit()
