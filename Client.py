if __name__ == '__main__':
    import pygame
    import sys
    import datetime
    logat = str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'CLIENT: '
    print(logat + 'Loading Rects Fight V1.6')
    sys.path.insert(0, './data')
    import game as g
    import var as v
    print(logat + 'Starting')
    pygame.init()
    g.title()
    g.char_select()
    while v.superloop:
        g.main()
    print(logat + 'Ending')
    pygame.quit()
